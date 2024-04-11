import json
from fastapi import FastAPI
from models import Patient


with open("patients.json", "r") as f:
    patient_list = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"

app = FastAPI()

patient_list = list[Patient]

@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patient_list.values()

@app.post("/patients/new")
async def new_patient(first_name: str, last_name: str, address: str, age: int) -> list[Patient]:
    return patient_list.append(first_name)

@app.put("/patients/{first_name}")
async def update_patient(first_name: str, last_name: str, address: str, age: int) -> list[Patient]:
    updated_patient = patient_list[first_name]
    return first_name

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> list[Patient]:
    patient_list.pop(first_name)