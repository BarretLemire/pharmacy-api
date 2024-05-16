import json
from fastapi import FastAPI, HTTPException
from models import Patient
from typing import List


with open("patients.json", "r") as f:
    patient_data = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"

app = FastAPI()

patient_list: List[Patient] = [Patient(**patient) for patient in patient_data]

@app.get("/patients", response_model=List[Patient])
async def get_patients() -> list[Patient]:
    return patient_list

@app.post("/patients/new")
async def new_patient(first_name: str, last_name: str, address: str, age: int) -> Patient:
    new_patient = Patient(first_name=first_name, last_name=last_name, address=address, age=age)
    patient_list.append(new_patient)
    return new_patient

@app.put("/patients/{first_name}")
async def update_patient(first_name: str, last_name: str, address: str, age: int) -> Patient:
    for idx, patient in enumerate(patient_list):
        if patient.first_name == first_name:
            updated_patient = Patient(first_name=first_name, last_name=last_name, address=address, age=age)
            patient_list[idx] = updated_patient
            return updated_patient
    raise HTTPException(status_code=404, detail="Patient not found")

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> list[Patient]:
    global patient_list
    updated_list = [patient for patient in patient_list if patient.first_name != first_name]
    if len(updated_list) == len(patient_list):
        raise HTTPException(status_code=404, detail="Patient not found")
    patient_list = updated_list
    return patient_list