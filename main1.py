from fastapi import FastAPI

app = FastAPI()

# Sample data
doctors = [
    {"id": 1, "name": "Dr. John Doe", "specialty": "Cardiologist"},
    {"id": 2, "name": "Dr. Jane Smith", "specialty": "Dermatologist"},
    {"id": 3, "name": "Dr. Alex Brown", "specialty": "Neurologist"}
] 


@app.get("/doctors")
def get_doctors():
    return doctors
