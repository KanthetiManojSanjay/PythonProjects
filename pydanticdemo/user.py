from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


u1 = User(id=1, name="John", age=35)
print(u1)
try:
    u2 = User(id=2, name="Bob", age="Twenty")
except Exception as e:
    print(e)
