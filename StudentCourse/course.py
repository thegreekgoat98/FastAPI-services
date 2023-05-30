from fastapi import FastAPI
from core.handler.student_handler import handler
from schema.models import Student,email
from constants.app_constants import endpoints
from fastapi import APIRouter

router=APIRouter()

obj=handler()

@router.get(endpoints.home) 
def fun():
    return obj.home()
    
@router.get(endpoints.show)
def show():
    return obj.show()

@router.post(endpoints.add) 
def add(student:Student):
    return obj.add(student)
    
@router.put(endpoints.update)
def update(roll:int,student:Student):
    return obj.update(roll,student)
    
@router.delete(endpoints.delete)
def delete(roll:int):
    return obj.delete(roll)

@router.post(endpoints.sendEmail)
def sendEmail(Email: email):
    return obj.send_email(Email)


    
