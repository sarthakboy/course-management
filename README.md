# Course Management System

A simple web application for managing courses, with distinct roles for admin and student users.

## Features

*   User Authentication (Registration and Login)
    *   Admin and Student roles
*   Admin Features
    *   Add New Courses
*   Student Features
    *   View Available Courses
    *   (Planned: Enroll in Courses)

## Technologies Used

**Backend:**

*   Flask
*   Flask-SQLAlchemy
*   Flask-CORS
*   SQLite (Database)

**Frontend:**

*   React
*   React Router DOM
*   CSS

## Setup Instructions

### 1. Clone the Repository

(You will do this after the project is on GitHub)

```bash
git clone <your_repository_url>
cd course_management
```

### 2. Backend Setup

Navigate to the project root directory:

```bash
cd path/to/your/project
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
# On Windows
venc\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-CORS
```

Initialize the database. This will create the `users.db` file.

```bash
python -c "from app import app, db; with app.app_context(): db.create_all()"
```

### 3. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install the required Node.js packages:

```bash
npm install
```

## How to Run the Application

### 1. Start the Backend

Navigate to the project root directory and run the Flask application:

```bash
cd path/to/your/project
venv\Scripts\activate # On Windows
source venv/bin/activate # On macOS/Linux
python app.py
```

The backend server will run at `http://127.0.0.1:5000`.

### 2. Start the Frontend

Navigate to the frontend directory and start the React application:

```bash
cd frontend
npm start
```

The frontend application will typically open in your browser at `http://localhost:3000`.

## API Endpoints

*   `POST /register`: Register a new user. Requires `username`, `password`, and `role` (admin or student).
*   `POST /login`: Login a user. Requires `username` and `password`. Returns user role and redirect URL on success.
*   `POST /course/add`: Add a new course (Admin only). Requires `name`, `duration`, and `description`.
*   `GET /course/enroll`: Get all available courses.

## Screenshots

(Add your screenshots here by replacing the placeholder markdown)

![Login Page Screenshot](images/login_page.png)

![Add Course Page Screenshot](images/add_course_page.png)

![Course Enroll Page Screenshot](images/course_enroll_page.png)

## Contributing

(Optional: Add contributing guidelines)

## License

(Optional: Add license information) 