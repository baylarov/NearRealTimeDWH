DROP SCHEMA IF EXISTS RTDWOrder;

CREATE SCHEMA  RTDWOrder;
SET search_path TO RTDWOrder;

CREATE TABLE position (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL
);

CREATE TABLE country (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL
);

CREATE TABLE city (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL,
	countryid int not null,
		FOREIGN KEY (countryid)
      REFERENCES country (id)
	
);

CREATE TABLE district (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL,
	cityid int not null,
		FOREIGN KEY (cityid)
      REFERENCES city (id)
);



CREATE TABLE branch (
	id serial PRIMARY KEY,
	name VARCHAR(500)   NOT NULL,
	countryid int not null,
	cityid int not null,
	districtid int not null,
	opendate timestamp not null,
	closedate timestamp null,
	FOREIGN KEY (countryid)
      REFERENCES country (id),
		FOREIGN KEY (cityid)
      REFERENCES city (id),
			FOREIGN KEY (districtid)
      REFERENCES district (id)
);


CREATE TABLE employees (
	id serial PRIMARY KEY,
	branchid int   NOT NULL,
	managerid int  null,
	name varchar(250) not null,
	gender varchar(50) null,
	birthdate timestamp not null,
	graduation varchar(250) not null,
	maritalstatus varchar(250) null,
	startdate timestamp not null,
	enddate timestamp null,
	worktype varchar(250) not null,
	FOREIGN KEY (branchid)
      REFERENCES branch (id)
);

CREATE TABLE customer (
	id serial PRIMARY KEY,
	name varchar(250)   NOT NULL,
	fulladdress varchar(500)  null,
	countryid int  null,
	cityid int  null,
	districtid int null,
	createdate timestamp not null,
	birthdate timestamp  null,
	graduation varchar(250)  null,
	maritalstatus varchar(250) null,
	profession varchar(250)  null,
	gender varchar(250)  null,
	FOREIGN KEY (countryid)
      REFERENCES country (id),
		FOREIGN KEY (cityid)
      REFERENCES city (id),
			FOREIGN KEY (districtid)
      REFERENCES district (id)
);

CREATE TABLE ordertype (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL
);



CREATE TABLE salesorder (
	id serial PRIMARY KEY,
	customerid int   NOT NULL,
	branchid int not null,
	amount numeric(10,2) not null,
	shipdate timestamp  null,
	canceldate timestamp null,
	orderdate timestamp not null,
	employeeid int not null,
	status int not null,
	typeid int not null,
	FOREIGN KEY (customerid)
      REFERENCES customer (id),
		FOREIGN KEY (branchid)
      REFERENCES branch (id),
			FOREIGN KEY (employeeid)
      REFERENCES employees (id),
				FOREIGN KEY (typeid)
      REFERENCES ordertype (id)
);


CREATE TABLE supplier (
	id serial PRIMARY KEY,
	name VARCHAR(500)   NOT NULL,
	countryid int not null,
	cityid int not null,
	districtid int not null,
	joindate timestamp not null,
	leavedate timestamp null,
	FOREIGN KEY (countryid)
      REFERENCES country (id),
		FOREIGN KEY (cityid)
      REFERENCES city (id),
			FOREIGN KEY (districtid)
      REFERENCES district (id)
);



CREATE TABLE category (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL,
	createdate timestamp not null
);


CREATE TABLE product (
	id serial PRIMARY KEY,
	name VARCHAR ( 250 )  NOT NULL,
	costprice numeric(10,2) not null,
	salesprice numeric(10,2) not null,
	quantity int not null,
	supplierid int not null,
	categoryid int not null,
	createdate timestamp not null,
		FOREIGN KEY (supplierid)
      REFERENCES supplier (id),
		FOREIGN KEY (categoryid)
      REFERENCES category (id)
);


CREATE TABLE orderdetails (
	id serial PRIMARY KEY,
	orderid int  NOT NULL,
	productid int  not null,
	quantity int not null,
	amount numeric(10,2) not null,
	supplierid int not null,
	createdate timestamp not null,
		FOREIGN KEY (orderid)
      REFERENCES salesorder (id),
		FOREIGN KEY (productid)
      REFERENCES product (id),
			FOREIGN KEY (supplierid)
      REFERENCES supplier (id)
);

















