from pydantic import BaseModel

class Student(BaseModel):
    name:str
    roll:int
    course:str
    price:float

class email(BaseModel):
    rec_email: str
    subject: str
    # body: str