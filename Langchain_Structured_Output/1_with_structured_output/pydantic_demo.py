from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str='de'
    age: Optional[int]=None
    email: EmailStr
    cgpa: float=Field(gt=0, lt=10,default=5 , description="CGPA must be between 0 and 10")
    

new_student={'name': 'pankaj', 'age': '30', 'email':'abc@gmail.com', 'cgpa': 8.5}
student=Student(**new_student)

print(student)
print(student.age)
print(type(student))

#print(student['email'])    # through an error because pydantic model is not subscriptable

student_dict=dict(student)
print(student_dict)
print(student_dict['email'])

student_json=student.model_dump_json()
print(student_json)