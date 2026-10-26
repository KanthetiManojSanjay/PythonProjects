from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Annotated


class Student(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=40)]
    age: Annotated[int, Field(ge=18, le=60)]
    gpa: Annotated[float, Field(ge=0, le=10)]
    email: EmailStr
    website: AnyUrl


s1 = Student(name="Bob", age=20, gpa=8.9, email="bob@gmail.com", website="http://www.bob.com")
print(s1)
try:
    s2 = Student(name="John", age=16, gpa=12.5, email="bob", website="nourl")
except Exception as e:
    print(e)
