# 🏥 Patient Management System

A simple **Patient Management System REST API** built using **Python and FastAPI**.

This project was created to practice backend development and understand how REST APIs work with CRUD operations, request validation, path parameters, query parameters, and API documentation using Swagger UI.

## 🚀 Features

* Create new patient records
* View all patients
* View a specific patient using Patient ID
* Update existing patient information
* Delete patient records
* Sort patients by name, age, or gender
* Sort records in ascending or descending order
* Automatic BMI calculation
* Automatic BMI-based health verdict
* Request validation using Pydantic
* Interactive API documentation using Swagger UI
* JSON file used for data storage

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **JSON**
* **Swagger UI / OpenAPI**

## 📌 API Endpoints

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/`                      | Welcome message            |
| GET    | `/about`                 | Information about the API  |
| GET    | `/view`                  | View all patients          |
| GET    | `/patients/{patient_id}` | View a specific patient    |
| GET    | `/sort`                  | Sort patient records       |
| POST   | `/create`                | Create a new patient       |
| PUT    | `/edit/{patient_id}`     | Update patient information |
| DELETE | `/delete/{patient_id}`   | Delete a patient           |

## 🧮 BMI Calculation

The API automatically calculates BMI using:

```text
BMI = Weight (kg) / Height² (m²)
```

Based on the calculated BMI, the API returns a health category:

| BMI          | Verdict     |
| ------------ | ----------- |
| Below 18.5   | Underweight |
| 18.5 – 24.99 | Normal      |
| 25 – 29.99   | Overweight  |
| 30 or above  | Obese       |

## 📋 Patient Data

Each patient record contains:

* Patient ID
* Name
* Age
* Gender
* Height
* Weight
* BMI
* Verdict

### Example

```json
{
  "id": "P001",
  "name": "Sanu",
  "age": 60,
  "gender": "Male",
  "height": 1.78,
  "weight": 75.0
}
```

The API automatically calculates:

```json
{
  "bmi": 23.67,
  "verdict": "Normal"
}
```

## 🔍 Sorting Patients

The `/sort` endpoint supports sorting by:

* `name`
* `age`
* `gender`

You can also choose the sorting order:

* `asc`
* `desc`

### Example

```text
/sort?sort_by=age&order_by=asc
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/PrernaPalsapure/Patient_Management_system.git
```

### 2. Navigate to the project directory

```bash
cd Patient_Management_system
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows:**

```bash
env\Scripts\activate
```

**Mac/Linux:**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 6. Run the application

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can:

* Test all API endpoints
* Send GET, POST, PUT and DELETE requests
* View request schemas
* Test validation
* Check API responses
* Explore the available endpoints

## 📂 Project Structure

```text
Patient_Management_system/
│
├── main.py
├── patients.json
├── README.md
├── LICENSE
└── VideoProject-ezgif.com-video-cutter.mp4
```

## 🎯 What I Learned

Building this project helped me understand:

* How FastAPI works
* REST API development
* CRUD operations
* GET, POST, PUT and DELETE methods
* Path parameters
* Query parameters
* Request bodies
* Data validation using Pydantic
* Pydantic `computed_field`
* BMI calculation through computed fields
* Error handling using HTTP exceptions
* JSON data handling
* API documentation with Swagger UI
* Running FastAPI applications using Uvicorn

## 🔮 Future Improvements

I would like to improve this project further by adding:

* 🗄️ Database integration using PostgreSQL or MongoDB
* 🔐 Authentication and authorization
* 🧪 Automated API testing
* 🔎 Better filtering and search functionality
* 📄 Pagination
* 🖥️ Frontend interface
* ☁️ Deployment using a cloud platform

## 🎥 Project Demo

A short demo of the Patient Management System is included in this repository.

The demo shows the API endpoints being tested through **Swagger UI**.

## 👩‍💻 Author

**Prerna Palsapure**

Learning and building projects with **Python, FastAPI, Machine Learning and AI/ML technologies**.

---

⭐ If you found this project useful, feel free to star the repository!
