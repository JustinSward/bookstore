.mode line

DROP TABLE IF EXISTS author;
CREATE TABLE author (
    author_id INTEGER PRIMARY KEY,
    a_name TEXT UNIQUE NOT NULL
);
INSERT INTO author (a_name) VALUES
    ("Charles Dickens"),
    ("Peter Behrens"),
    ("Jerome David Salinger"),
    ("Mohammed L. A. Sherif"),
    ("Minh Ng"),
    ("Sally Yomato");



DROP TABLE IF EXISTS book_authors;
CREATE TABLE book_authors (
    isbn INTEGER,
    author_id INTEGER
);
INSERT INTO book_authors (isbn,author_id) VALUES
    (9780553211764,1),
    (9780812978001,2),
    (9780553250251,3),
    (9781853260049,1);



DROP TABLE IF EXISTS genre;
CREATE TABLE genre (
    genre_id INTEGER PRIMARY KEY,
    genre_name TEXT UNIQUE NOT NULL
);
INSERT INTO genre (genre_name) VALUES
    ("Non-fiction"),
    ("Fiction"),
    ("Science Fiction"),
    ("Textbook"),
    ("Comedy"),
    ("Classic");



DROP TABLE IF EXISTS book;
CREATE TABLE book (
    isbn INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre_id INTEGER,
    publisher_id INTEGER NOT NULL,
    publishyear INTEGER,
    numpages INTEGER,
    currentprice REAL NOT NULL,
    qtyavail INTEGER NOT NULL,
    qtyonorder INTEGER NOT NULL
);
INSERT INTO book (isbn,title,genre_id,publisher_id,publishyear,numpages,currentprice,qtyavail,qtyonorder) VALUES
    (9780553211764,"A Tale of Two Cities",6,1,1989,369,14.99,5,0),
    (9780812978001,"The Law of Dreams",2,1,2007,416,9.99,10,5),
    (9780553250251,"The Catcher in the Rye",6,2,1964,214,17.99,1,0),
    (9781853260049,"Great Expectations",2,3,1992,395,22.99,7,0);



DROP TABLE IF EXISTS publisher;
CREATE TABLE publisher (
    publisher_id INTEGER PRIMARY KEY,
    p_name TEXT NOT NULL,
    p_email TEXT NOT NULL,
    p_telephone TEXT NOT NULL,
    p_street TEXT NOT NULL,
    p_city TEXT NOT NULL,
    p_stateprov TEXT NOT NULL,
    p_postalzip TEXT NOT NULL,
    p_country TEXT NOT NULL,
    p_bankaccountnum TEXT NOT NULL,
    p_commissionpct REAL NOT NULL
);
INSERT INTO publisher (p_name,p_email,p_telephone,p_street,p_city,p_stateprov,p_postalzip,p_country,p_bankaccountnum,p_commissionpct) VALUES
    ("Random House Publishing Group","info@penguinrandomhouse.com","8007333000","1745 Broadway Avenue","Manhattan","New York","15284","United States","00048273-400",0.9),
    ("Bantam Books","help@bantambooks.com","2025550011","88 81st Street N","New York","New York","15205-1948","United States","002-487640283",0.75),
    ("Wordsworth Classics","contact_us@wordsworth-eidtions.com","+44 (0) 1920 465167","PO Box 13147","Standsted", "N/A","CM211BT", "England","55-7850008",1.05);



DROP TABLE IF EXISTS commissions;
CREATE TABLE commissions (
    payment_id INTEGER PRIMARY KEY,
    publisher_id INTEGER NOT NULL,
    transaction_no TEXT NOT NULL,
    amount_paid REAL NOT NULL,
    payment_year INTEGER NOT NULL,
    payment_month INTEGER NOT NULL,
    payment_day INTEGER NOT NULL
);
INSERT INTO commissions (publisher_id,transaction_no,amount_paid,payment_year,payment_month,payment_day) VALUES
    (1,"00018042",101.09,2022,11,1),
    (1,"00018273",204.50,2022,12,1),
    (1,"00019002",101.09,2022,11,1);



DROP TABLE IF EXISTS order_manifest;
CREATE TABLE order_manifest (
    order_id INTEGER,
    isbn INTEGER,
    pricepaid REAL NOT NULL,
    qty INTEGER NOT NULL
);
INSERT INTO order_manifest (order_id,isbn,pricepaid,qty) VALUES
    (1,9780553211764,14.99,1),
    (1,9780812978001,9.99,1),
    (2,9780553250251,17.99,3);



DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    u_id INTEGER,
    order_year INTEGER NOT NULL,
    order_month INTEGER NOT NULL,
    order_day INTEGER NOT NULL,
    bill_street TEXT NOT NULL,
    bill_city TEXT NOT NULL,
    bill_stateprov TEXT NOT NULL,
    bill_postalzip TEXT NOT NULL,
    bill_country TEXT NOT NULL,
    ship_street TEXT NOT NULL,
    ship_city TEXT NOT NULL,
    ship_stateprov TEXT NOT NULL,
    ship_postalzip TEXT NOT NULL,
    ship_country TEXT NOT NULL,
    shipping_courier TEXT,
    ship_trackingno TEXT,
    shipping_cost REAL NOT NULL,
    subtotal REAL NOT NULL,
    tax REAL NOT NULL,
    grandtotal REAL NOT NULL,
    creditcardnum TEXT NOT NULL,
    creditcardexp TEXT NOT NULL,
    transactionid TEXT NOT NULL
);
INSERT INTO orders (u_id,order_year,order_month,order_day,bill_street,bill_city,bill_stateprov,bill_postalzip,bill_country,ship_street,ship_city,
                    ship_stateprov,ship_postalzip,ship_country,shipping_courier,ship_trackingno,shipping_cost,subtotal,tax,grandtotal,creditcardnum,
                    creditcardexp,transactionid) VALUES
    (4,2022,11,30,"52 York Ave","Toronto","Ontario","J9P 6W7","Canada","52 York Ave","Toronto","Ontario","J9P 6W7","Canada","UPS","0009387478CA1",
        10.00,34.98,4.55,39.53,"8888555544440000","03/24","054985"),
    (3,2022,12,01,"2 Richmond Road","Los Angeles","California","71058","United States","2 Richmond Road","Los Angeles","California","71058","United States","FedEx","893HF8398",
        15.00,68.97,8.97,77.94,"0000111122223333","12/23","858875054");



DROP TABLE IF EXISTS useraccounts;
CREATE TABLE useraccounts (
    u_id INTEGER PRIMARY KEY,
    u_pw TEXT NOT NULL,
    u_fname TEXT NOT NULL,
    u_lname TEXT NOT NULL,
    u_telephone TEXT NOT NULL,
    u_email TEXT UNIQUE NOT NULL,
    u_accttype BOOL NOT NULL,
    u_street TEXT,
    u_city TEXT,
    u_stateprov TEXT,
    u_postalzip TEXT,
    u_country TEXT NOT NULL
);
INSERT INTO useraccounts (u_pw,u_fname,u_lname,u_telephone,u_email,u_accttype,u_country) VALUES
    ("admin","Store","Owner","6132555411","justin@carleton.ca",1,"Canada"),
    ("123","Ed","Smith","4165552500","edsmith@yahoo.biz",0,"Canada");
INSERT INTO useraccounts (u_pw,u_fname,u_lname,u_telephone,u_email,u_accttype,u_street,u_city,u_stateprov,u_postalzip, u_country) VALUES 
    ("qwe","Amar","Khan","3035558473","amar@khan.ca",0,"2 Richmond Road","Los Angeles","California","71058","United States"),
    ("asd","Rachelle","Louis","5196825099","rl@abcinc.ca",0,"10-387 Rue De La Fontaine","Montreal","Quebec","H8C3G0","Canada"),
    ("qwe","Frank","Vincent","4165558877","frank@frank.frank",0,"52 York Ave","Toronto","Ontario","J9P 6W7","Canada");
