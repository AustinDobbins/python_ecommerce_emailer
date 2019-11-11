import smtplib 
import mysql.connector
import re


class birthday_email():
    def check_birthday(self):
        global user_data_pull
        id_list = [] 
        query = 'SELECT first_name, customer_email FROM customer_info WHERE customer_birthdate = CURDATE()'
        mycursor.execute(query)
        user_data_pull = mycursor.fetchall()

    def get_email_template(self): 
        global email
        file = open('bday_email.txt', mode='r')
        email = file.read()
        
    def organize_data(self):
        global first_name_list, email_list
        first_name_list = []
        email_list = []
        for data in user_data_pull:
            first_name_list.append(data[0])
            email_list.append(data[1])

    def create_email_templates(self):
        global email_template_list 
        email_template_list = []
        for name in first_name_list:
            email_template_list.append(email.replace('<FIRST-NAME>', name))

    def send_email(self):
        global email_number
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo() 
        mail.starttls()
        mail.login(SENDER_EMAIL, EMAIL_PASSWORD)
        email_number = 0
        for i in email_template_list:
            mail.sendmail(SENDER_EMAIL, email_list[email_number], i)
            email_number += 1
        mail.close()
        print(email_number + ' birthday emails sent!')

class loyalty_email():
    def check_total_spendings(self):
        global user_data
        query = '''
        SELECT first_name, customer_email 
        FROM customer_info 
        WHERE customer_id = 
            (SELECT customer_id 
            FROM orders
            WHERE COUNT(order_cost) > 100)
            GROUP BY customer_id 
            '''
        mycursor.execute(query)
        user_data = mycursor.fetchall()

    def get_email_template(self): 
        global email
        file = open('loyal_email.txt', mode='r')
        email = file.read()

    def organize_data(self):
        global first_name_list, email_list
        first_name_list = []
        email_list = []
        for data in user_data:
            first_name_list.append(data[0])
            email_list.append(data[1])

    def create_email_templates(self):
        global email_template_list 
        email_template_list = []
        for name in first_name_list:
            email_template_list.append(email.replace('<FIRST-NAME>', name))

    def send_email(self):
        global loyal_email_number
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo() 
        mail.starttls()
        mail.login(SENDER_EMAIL, EMAIL_PASSWORD)
        loyal_email_number = 0
        for i in email_template_list:
            mail.sendmail(SENDER_EMAIL, email_list[loyal_email_number], i)
            loyal_email_number += 1
        mail.close()
        print(loyal_email_number + ' loyalty emails sent!')


SENDER_EMAIL = ''
EMAIL_PASSWORD = ''

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'emailer'
    )
mycursor = mydb.cursor()

bday_emailer = birthday_email()
bday_emailer.check_birthday()
bday_emailer.get_email_template()
bday_emailer.organize_data()
bday_emailer.create_email_templates()
bday_emailer.send_email()

loyal_email = loyalty_email()
loyal_email.check_total_spendings()
loyal_email.get_email_template()
loyal_email.organize_data()
loyal_email.create_email_templates()
loyal_email.send_email()