# <b>E-Commerce Email Marketing Tool</b>

## <b>Getting Started</b>

These instructions will explain everything necessary to get this Python script working properly.

### <b>Preruisites </b>

You will need to make sure you have the following install on your machine:

> Python 3.6

> MYSQL 8.0 Server

> Python MYSQL-Connector package

###  <b>Installing</b>
Download and install Python at: 
> https://www.python.org/downloads/

Download and install MySQL at:
> https://dev.mysql.com/downloads/windows/installer/8.0.html

Install Python dependencies:

CD into the github repo folder after where you cloned it from github
> pip install -r requirements.txt

### <b>How to Use </b>
<b>Filling the database: </b>

First you will need to manually insert test data into the MySQL tables.

<b>Altering the Python script to work with sender email:  </b>

On line 94 put your gmail account address in the quotes. 

On line 95 put the password for that gmail account in the quotes. 

On line 100 put your MySQL root password in quotes

<b>Once the database is filled with desired data run:</b>
> python send.py

The script will query the MySQL database to pull data on anyone that has a birthday today or has spent over $100 in the ecommerce store. The script will than compile a customized email and send it to each applicable recipient.