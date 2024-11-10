Employee Management REST API

This is a Django-based REST API for managing employee records. It provides endpoints for creating, retrieving, searching, and deleting employee data. This API is built using Django REST Framework.

Features:
Create Employee: Add new employee details to the database.
Retrieve Employees: Get a list of all employees or fetch details of a specific employee by ID.
Update Employee: Update info a particular employee by ID
Search by Name: Search for employees by name.
Delete Employee: Delete an employee record by ID.

Installation:
1. Clone the repository
2. create and activate a django virtual environment
3. Install dependencies (Django, restframework, etc..)
4. Run migrations (py manage.py makemigrations, py manage.py migrate)
5. Start the server

API Endpoints:
POST: /create-employee/  Create a new Employee
GET:  /create-empoloyee/ List existing employee
GET: /retrieve-employee/<id> Retrieve existing employee using ID
PUT: /update-employee/<id> Update an employee by their ID
GET: /search-employee/<name> Search employee using name
DELETE: /delete-employee/<id> Delete employee by their ID

Technologies Used:
1. Django: Web framework for building API.
2. Django REST framework: Toolkit for building RESTful APIs.

Assets:
1. ![Create-list](https://github.com/user-attachments/assets/37e9603c-7c9e-48d1-9231-4bb546466fff)
2. ![Available-paths](https://github.com/user-attachments/assets/3cb430dd-a431-4232-b3b5-e092d9c0f75c)

