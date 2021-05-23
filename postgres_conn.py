import psycopg2
import time as tm


class DbConnection:
    def __init__(self, username='postgres', password='root', hostname='localhost', port='5432', database='postgres'):
        self.connection = psycopg2.connect(host=hostname, database=database, user=username, password=password,
                                           port=port)
        if self.connection:
            print('Connection is success.')

    # def get_conn(self):
    #     return self.connection

    def get_conn(self):
        calisma_sayi = 3
        bekleme_suresi = 60
        tekrar_denesin_mi = True
        deneme_sayi = 0

        while tekrar_denesin_mi and deneme_sayi < calisma_sayi:
            try:
                cnxn = self.connection
                tekrar_denesin_mi = False
                return cnxn
            except(Exception) as error:
                print("Retrying Postgres connection after {} seconds. More: \n{}".format(bekleme_suresi, error))
                deneme_sayi += 1
                tm.sleep(bekleme_suresi)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class ConnectionCursor:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = DbConnection().get_conn()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            self.conn.rollback()
        else:
            self.cursor.close()
            self.conn.commit()
