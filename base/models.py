from django.db import models
import mysql.connector


MyDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password='1/2/3/4/5/6/7/8/9/10',
    database="crm_db",
)

coursorObj = MyDB.cursor()
coursorObj.execute("CREATE DATABASE IF NOT EXISTS crm_db")
print("Database created successfully")
MyDB.database = "crm_db"
