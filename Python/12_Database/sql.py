# Write a programs to understand GUI database connectivity to perform CRUD operations in python using MYSQL

# ************** 1.Installation of mysql ******************** 
#     (In Ubuntu Terminal):
#     sudo apt-get install python3-mysql.connector
#     sudo apt-get install python-dev libmysqlclient-dev
#     sudo apt-get install python-mysql

#     import mysql.connector(Inside Python shell)


# *********2. Creating Databases and Tables **************
#       (In Ubuntu Terminal):
#       create database xyz
#       ;
#       use xyz
#       create table marks(roll no int, UT1 int, UT2 int)
#       ;
#       insert into marks values(19,20,20)
#       ;
#       insert into marks values(29,23,30)
#       select * from marks;


#*************3. Granting Permissions ****************
#     (In Ubuntu Terminal):
#       create user xyz identified by 'xyz';
#       grant all on 'previously created database'.* to xyz@localhost identified by 'xyz'
#       flush priviliges

import MySQLdb as db 
HOST = "localhost" 
PORT = 3306
USER = "apsit17104074" 
PASSWORD = "apsit17104074" 
DB = "SEIT17104074"
connection = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
print ("Connection successful to ",HOST) 
dbhandler = connection.cursor()



