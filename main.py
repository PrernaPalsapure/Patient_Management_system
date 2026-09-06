from fastapi import FastAPI,Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field , computed_field
from typing import Annotated, Literal, Optional
import json

def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json" , "w") as f:
        json.dump(data , f)


data = load_data()
app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str , Field(..., description="The ID of the Patient",example="P001")]
    name : Annotated[str, Field(..., description="Name of the Patient" , max_length=50)]
    age : Annotated[int, Field(..., description="Age of the Patient" , gt=0 , lt=120)]
    gender : Annotated[Literal["Male" , "Female" , "Others"] , Field(..., description="Gender of the Patient")]
    height : Annotated[float,Field(...,description="Height of the Patient in mtrs" , gt=0)]
    weight : Annotated[float, Field(...,description="Weight of the Patient in kgs", gt=0)]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi <25 :
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):
    name : Annotated[Optional[str],Field(default=None)]
    age  :Annotated[Optional[int] ,Field(default=None , gt=0, lt=120)]
    gender : Annotated[Optional[Literal["Male" , "Female" , "Others"]] ,Field(default=None)]
    height : Annotated[Optional[float] , Field(default=None , gt=0)]
    weight : Annotated[Optional[float] , Field(default=None , gt=0)]


@app.get("/")
def hello():
    return{"message":"Patient Management System"}


@app.get("/about")
def about():
    return{"message":"This is a simple Patient Management System API built using FastAPI."}


@app.get("/view")
def view():
    data=load_data()
    return data


@app.get("/patients/{patient_id}")
def view_patients(patient_id : str = Path(..., description="The ID of the patient to retrieve" , example="P001")):
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by : str =Query(..., description="The field to sort the patients by" , example='age'), order_by : str=Query('asc',description="The order to sort the patients by, either 'asc' or 'desc'", example='asc')):

    valid_fields=['name','age','gender']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid Selection.Please select from {valid_fields}')

    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400 , detail="Invalid order_by value.please select either 'asc' or 'desc'")

    data=load_data()

    sort_order=True if order_by=='desc' else False

    sorted_data=sorted(data.values() , key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.post("/create")
def add_data(patient : Patient):
    
    #load data
    data=load_data()

    #check if Patient data already exists
    if patient.id in data:
        raise HTTPException(status_code=400 , detail="Patient already exists")

    #Add new Patient to the data
    data[patient.id]=patient.model_dump(exclude={'id'})

    #save into json file
    save_data(data)

    return JSONResponse(status_code= 201 , content={"message":"Patient Created Successfully"})

@app.put("/edit/{patient_id}")
def update_patient(patient_id : str , patient_update : PatientUpdate):
    
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404 , detail="Patient Not Found")

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key]= value
    

    #existing data -> pydantic object ->updated bmi,verdict
    
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    #pydantic object -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude={'id'})

    #add this Dict to data
    data[patient_id] = existing_patient_info
    
    #save data 
    save_data(data)

    return JSONResponse(status_code=200 , content={'message' : 'Patient Updated Successfully'})

@app.delete("/delete/{patient_id}")
def delete_data(patient_id : str):
    
    #load the data
    data=load_data()

    #checks if patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")

    #delete patient data
    del data[patient_id]

    #save the updated data
    save_data(data)

    return JSONResponse(status_code=200, content={"message" : "Patient Deleted Successfully"})


