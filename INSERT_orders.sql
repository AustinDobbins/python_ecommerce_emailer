# this data will work to trigger the loyatly_email()
# make sure to run the INSERT statement for the customer_info table prior to running this insert statement
# customer_id is the foreign key that creates the relation between the two tables 

INSERT INTO orders (customer_id, order_cost, tracking_num, order_date)
VALUES(1, 59.99, '123456778812', '2019-01-01'), (2, 79.99, '123456778812', '2018-08-08'), 
(3, 34.99, '123456778812', '2018-08-08'), (1, 44.99, '123456778812', '2018-09-09'),
(4, 59.99, '123456778812', '2019-09-09'), (3, 89.99, '123456778812', '2019-09-09')