from pprint import pprint

student = {
    "name" : "taruna",
    "age" : 22,
    "gender" : "male",
    "film" : "action",
}

student.pop("gender")
pprint(student)

student.popitem()
pprint(student)

student.clear()
pprint(student)