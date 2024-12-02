# Todo API

A simple RESTful Todo API built using Django, Django REST Framework, and PostgreSQL. The API allows users to manage tasks with features like authentication, CRUD operations for todos, and token-based authentication via JWT (JSON Web Token).

## Features

- **User Authentication**: Sign up, login, and authenticate users using JWT.
- **Todo Management**: CRUD operations for managing todos.
- **Advanced Todo Features**:
  - Due date management.
  - Priority levels for tasks.
  - Todo statuses like "in progress", "completed", etc.
- **Admin Tools**: Admin access to manage users and todos.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite3
- **Authentication**: Simple JWT for token-based authentication

## Installation

Follow the steps below to set up the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/todo-api.git
cd todo-api
```
### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
```bash
SECRET_KEY=your-secret-key
EMAIL_HOST_USER=your_gmail
EMAIL_HOST_PASSWORD=your_password
```
### 5. Run Database Migrations
```bash
python manage.py migrate
```
### 6. Create Superuser
```bash
python manage.py createsuperuser
```
### 7. Run the Development Server
```bash
python manage.py runserver
```
### 8. Run Celery
```bash
celery -A your_project_name worker --loglevel=info
```
### 9. Install Redis (Required for Celery)
```bash
sudo apt install redis-server
sudo systemctl start redis-server
```
## Contributing
- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.
