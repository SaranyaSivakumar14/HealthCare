from fastapi import FastAPI

app = FastAPI()

# Sample data
doctors = [
{
  "id": 1,
  "name": "Dr. Paul",
  "specialty": "Cardiologist"
},
{
  "id": 2,
  "name": "Dr. Jane Smith",
  "specialty": "Dermatologist"
},
{
  "id": 3,
  "name": "Dr. Alex Brown",
  "specialty": "Neurologist"
},
{
  "id": 4,
  "name": "Dr. John Doe",
  "specialty": "Cardiologist"
},
{
  "id": 5,
  "name": "Dr. Martin",
  "specialty": "Cardiologist"
},
{
  "id": 6,
  "name": "Dr. Smith",
  "specialty": "Cardiologist"
},
{
  "id": 7,
  "name": "Dr. Mary",
  "specialty": "Cardiologist"
},
{
  "id": 8,
  "name": "Dr.Ravi ",
  "specialty": "Cardiologist"
},
{
  "id": 9,
  "name": "Dr. Selvi",
  "specialty": "neurologist"
},
{
  "id": 10,
  "name": "Dr.Durai",
  "specialty": "Dermatologist"
},
{
  "id": 11,
  "name": "Dr.palanisamy",
  "specialty": "phychologist"
},
{
  "id": 12,
  "name": "Dr.mahalakshmi",
  "specialty": "Dermatologist"
},
{
  "id": 13,
  "name": "Dr.velusamy",
  "specialty": "phychologist"
},
{
  "id": 14,
  "name": "Dr.lakshmi",
  "specialty": "Dermatologist"
},
{
  "id": 15,
  "name": "Dr. usha",
  "specialty": "neurologist"
},
{
  "id": 16,
  "name": "Dr.Durairaj",
  "specialty": "Dermatologist"
},
{
  "id": 17,
  "name": "Dr.samy",
  "specialty": "phychologist"
},
{
  "id": 18,
  "name": "Dr.maha",
  "specialty": "Dermatologist"
},
{
  "id": 19,
  "name": "Dr.velusamy",
  "specialty": "phychologist"
},
{
  "id": 20,
  "name": "Dr.subbulakshmi",
  "specialty": "Dermatologist"
}
] 


@app.get("/doctors")
def get_doctors():
    return doctors
