CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(255),
    email VARCHAR(255),
    country VARCHAR(100),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    product_category VARCHAR(100),
    amount NUMERIC(10,2),
    payment_method VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS marketing_campaigns (
    campaign_id INT PRIMARY KEY,
    customer_id INT,
    channel VARCHAR(100),
    campaign_date DATE,
    campaign_cost NUMERIC(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id INT PRIMARY KEY,
    customer_id INT,
    ticket_date DATE,
    issue_type VARCHAR(100),
    resolution_hours NUMERIC(6,1),
    satisfaction_score INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
