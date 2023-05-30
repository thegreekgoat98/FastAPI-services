from core.db.mongodb import Mongo
from schema.models import Student,email
from constants.aggregationPipelines import agg_code

from json2html import *

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


obj=Mongo()

class handler:
    def home(self):
        return {"This is for student registration into a course."}

    def show(self):
        result = list(obj.myDB.find({}))
        final_list = []
        for stud in result:
            del stud["_id"]
            final_list.append(stud)
        return {"The data for all students ": final_list}

    def add(self,student:Student):
        if list(obj.myDB.find({"roll":student.roll})) == []:
            obj.myDB.insert_one(student.dict())
            return {"Success":"Added student in the course successfully"}
        else:
            return {"Error":"Cannot add student, already enrolled in a course"}
    
    def update(self,roll:int,student: Student):
        if list(obj.myDB.find({"roll":student.roll})) == []:
            if list(obj.myDB.find({"roll":roll})) == []:
                return {"Error":"Student not enrolled in any course"}
            else:
                obj.myDB.update_one({"roll":roll},{"$set":student.dict()})
                return {"Success":"Updated succesfully"}
        else:
            return {"Error":"Cannot update to this roll, roll already present"}
    
    def delete(self,roll:int):
        if list(obj.myDB.find({"roll":roll})) == []:
            return {"Error":"Student has not enrolled in any course till now"}
        obj.myDB.delete_one({"roll":roll})
        return {"Success":"Deleted the student from the course"}
    
    def aggregate(self):
        a=obj.myDB.aggregate(agg_code)    
        a_list=list(a)
        return a_list[0]["total"]
    
    def send_email(self,Email: email):
        # Set up the email details
        sender_email = "ranjanchinmoy@gmail.com"
        sender_password = "fjxauommuysxprxg"
        receiver_email = Email.rec_email

        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = Email.subject
    
        #manually added
        body = self.aggregate() 
        body=str(body)

        #manually added
        all_students_list=self.show() 
        table=json2html.convert(json=all_students_list) #for table
        # Add the body to the email
        message.attach(MIMEText("The total cost of all courses student have enrolled is: ₹"+body+"\n\n", "plain"))
        message.attach(MIMEText("\n\nStudent Table: "+table,"html"))


        try:
        # Create a secure connection to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
        # Login to the sender's email account
            server.login(sender_email, sender_password)
         # Send the email
            server.send_message(message)
        # Close the connection
            server.quit()
            return {"message": "Email sent successfully"}
        except Exception as e:
            return {"message": str(e)}
