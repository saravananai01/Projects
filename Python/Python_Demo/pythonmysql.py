import mysql.connector

con=mysql.connector.connect(

host="192.168.1.240",
user="AIBATCH01",
password="AI@123",
database="ai_saravanan"

)


result=con.cursor()
result.execute("show tables")
result_show=result.fetchall()
for x in result_show:
    print(x)