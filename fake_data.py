from postgres_conn import ConnectionCursor
from faker import Faker
import random
from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def positions():
    positions = ['Junior', 'Mid-level', 'Senior', 'Expert', 'Manager', 'Team-lead', 'Director', 'C-level']
    with ConnectionCursor() as conn:
        for i in positions:
            postgres_insert_query = '''insert into RTDWOrder.position (name) VALUES (%s)'''
            record_to_insert = (i,)
            conn.execute(postgres_insert_query, record_to_insert)


def employees():
    fake = Faker()

    with ConnectionCursor() as cursor:
        truncate_query = 'truncate table RTDWOrder.employees cascade'
        cursor.execute(truncate_query)
        max_id_branch = "select max(id) from RTDWOrder.branch"
        cursor.execute(max_id_branch)
        max_branch_id = cursor.fetchone()[0]
        start = 0
        while start <= 5:
            gender_list = ['Male', 'Female', 'Transgender', None]
            start_birtdate = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
            end_birtdate = datetime.strptime('1/1/2003 4:50 AM', '%m/%d/%Y %I:%M %p')
            graduation_list = ['PHD', 'Master', 'Bachelor', 'College', 'High School', 'Elementary school']
            maritalstatus_list = ['Single', 'Married', 'Divorced', None]
            worktype_list = ['Full-time', 'Half-time', 'Remote', 'Freelance']

            branch_id = random.randint(1, max_branch_id)

            branch_open_date_query = "select opendate from RTDWOrder.branch where id='{}'".format(branch_id)
            cursor.execute(branch_open_date_query)
            branch_open_date = cursor.fetchone()[0]
            employee_start_date = random_date(branch_open_date, datetime.today())

            name = fake.name()
            gender = random.choice(gender_list)
            birthdate = random_date(start_birtdate, end_birtdate)
            graduation = random.choice(graduation_list)
            marital_status = random.choice(maritalstatus_list)
            worktype = random.choice(worktype_list)
            employee = "{} - {} - {} - {} - {} - {} - {} - {}".format(branch_id, name, gender, birthdate.date(),
                                                                      graduation,
                                                                      marital_status, worktype, employee_start_date)

            # print(employee)
            try:
                title = ['branchid', 'name', 'gender', 'birthdate', 'graduation', 'maritalstatus', 'worktype',
                         'startdate']
                cols = ",".join([str(c) for c in title])
                insert_query = "insert into RTDWOrder.employees(" + cols + ") values (%s,%s,%s,%s,%s,%s,%s,%s)"

                data = (1, f"{name}", f"{gender}", f"{birthdate}", f"{graduation}",
                        f"{marital_status}", f"{worktype}", f"{employee_start_date.date()}")
                cursor.execute(insert_query, data)
                print("Inserted data: '{}'".format(employee))
            except(Exception) as exc:
                print(exc)

            start += 1


# employees()
# managerid -> kendisi haric ayni branche bagli employeeid,(en sonda)
# startdate -> random date after branch start date,
# enddate -> random date btw branch start-end dates,
