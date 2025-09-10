from django.db import models
import mysql.connector


# MyDB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password='1/2/3/4/5/6/7/8/9/10',
#     database="crm_db",
# )

# coursorObj = MyDB.cursor()
# coursorObj.execute("CREATE DATABASE IF NOT EXISTS crm_db")
# print("Database created successfully")
# MyDB.database = "crm_db"

class Record(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name