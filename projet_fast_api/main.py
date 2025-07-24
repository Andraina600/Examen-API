from fastapi import FastAPI, Request
from starlette.responses import Response 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/hello")
def read_root():
    return JSONResponse({"message" : "Hello word"} , status_code=200)


@app.get("/welcome")
def welcome_name(name: str):
        return {"Welcome " + name}


class StudentModel(BaseModel):
    reference : str
    firstName: str
    lastName: str
    age: int
    
student_store: List[StudentModel] = []

def serialized_stored_students():
    student_converted = []
    for student in student_store:
        student_converted.append(student.model_dump())
    return student_converted


@app.post("/students")
def create_event(student: List[StudentModel]):
    for students in student:
        student_store.append(students)
    return JSONResponse({"message": "Événement ajouté"} , status_code=201)

@app.get("/students")
def list_students(request : Request):
    return  JSONResponse({"students" : serialized_stored_students()}, status_code=200)

@app.put("/students")
def update_multiple_events(students: List[StudentModel]):
    for i, student in enumerate(students):
        if i < len(student_store):
            student_store[i] = student
        else:
            student_store.append(student)

    return {"students": serialized_stored_students()}
