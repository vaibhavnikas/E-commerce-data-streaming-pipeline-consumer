CREATE TABLE fact_transaction(
    transaction_id INT,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    billed_amount INT NOT NULL,
    location_id INT,
    date_id varchar(50),
    PRIMARY KEY(transaction_id, product_id)
);

CREATE TYPE gendertype AS ENUM('F', 'M');
CREATE TABLE dim_customer(
    id INT PRIMARY KEY,
    firstname varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    phone varchar(20) NOT NULL,
    email varchar(200) NOT NULL,
    gender gendertype NOT NULL
);

CREATE TABLE dim_product(
    id INT PRIMARY KEY,
    name varchar(250) NOT NULL,
    category_id INT,
    price INT NOT NULL
);

CREATE TABLE dim_category(
    id INT PRIMARY KEY,
    name varchar(100) NOT NULL
);

CREATE TABLE dim_location(
    id INT PRIMARY KEY,
    pincode INT NOT NULL,
    locality_name varchar(100) NOT NULL,
    city varchar(50) NOT NULL,
    state varchar(50) NOT NULL
);

CREATE TABLE dim_date(
    id varchar(50) PRIMARY KEY,
    day INT NOT NULL,
    day_of_week INT NOT NULL,
    month INT NOT NULL,
    month_name varchar(20) NOT NULL,
    year INT NOT NULL
);


ALTER TABLE fact_transaction
ADD CONSTRAINT fk_customer_id
FOREIGN KEY (customer_id)
REFERENCES dim_customer (id);

ALTER TABLE fact_transaction
ADD CONSTRAINT fk_product_id
FOREIGN KEY (product_id)
REFERENCES dim_product (id);

ALTER TABLE fact_transaction
ADD CONSTRAINT fk_location_id
FOREIGN KEY (location_id)
REFERENCES dim_location (id);

ALTER TABLE fact_transaction
ADD CONSTRAINT fk_date_id
FOREIGN KEY (date_id)
REFERENCES dim_date (id);

ALTER TABLE dim_product
ADD CONSTRAINT fk_category_id
FOREIGN KEY (category_id)
REFERENCES dim_category (id);
