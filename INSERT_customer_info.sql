# replace all the fields in the values section to relevant data to test the python script
# most importantly put a email to send your test emails to
# if wanting to trigger the birthday_email() 
# make sure to set one or more birthdates to todays date

INSERT INTO emailer.customer_info (first_name, last_name, customer_address, customer_birthdate, customer_email)
VALUES('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com'),('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com'),
('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com'),('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com'),
('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com'),('alex', 'smith', '123 W. Murica ln', '1994-04-04', 'asdfasdf@gmail.com')
;