# Train Ticket Booking System

## Overview
This project is a Train Ticket Booking System built with Flask, PostgreSQL, and JWT for authentication. It allows users to book seats on trains while ensuring that concurrent bookings are handled correctly. The application follows a modular architecture, separating concerns for better maintainability and scalability.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- PostgreSQL
- pip (Python package installer)

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/snehshahh/irctc-assignment.git
   cd app

2. **Make Virtual ENV file**
   python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies**
   pip install -r requirements.txt

4. **Run The App**
   python app.py

### Sample Paramaeters for Testing In Postman
1. **Users: Register**
    URL:http://127.0.0.1:5000/user/register
    PROTOCOL:POST
    BODY:
    {
        "username":"Test",
        "password":"Test7634@",
        "email":"Test7634@gmail.com",
        "role":"Admin"
    }

2. **Users: Login**
    URL:http://127.0.0.1:5000/user/login
    PROTOCOL:POST
    BODY:
    {
        "username":"Test",
        "password":"Test7634@",
        "email":"Test7634@gmail.com",
        "role":"Admin"
    }

3. **Train: Add Trains**
    URL:http://127.0.0.1:5000/trains/add_train
    PROTOCOL:POST
    BODY:
    {
        "train_name": "Medium Train",
        "source_station": "Station E",
        "destination_station": "Staion F",
        "total_seats": 100,
        "api_key":"c1af7e8a0fc82c0d487ef1a08443eb8762e92f5a22c9662403d788b6ab490cbf"
    }

4. **Train: Get Available Trains**
    URL:http://127.0.0.1:5000/trains/get_available_trains?FromStation=Station A&ToStation=Station B
    PROTOCOL:GET

5. **Train: Book Ticket**
    URL:http://127.0.0.1:5000/bookings/book_ticket
    PROTOCOL:POST
    BODY:
    {
        "train_id": 1,
        "no_of_seats_required": 2
    }

4. **Train: Get Booking Details**
    URL:http://127.0.0.1:5000/bookings/booking_details?BookingId=35a917d0-528f-4dd7-bf26-942c18d15c03
    PROTOCOL:GET


## Architecture

The project follows a structured architecture with the following components:


### Project Components

- **`app/__init__.py`**: Initializes the Flask application, loads configurations, and registers blueprints.
- **`app/config.py`**: Contains configuration settings, including database URLs and secret keys for JWT.
- **`app/models.py`**: Defines data models, including the structure for users, trains, and bookings.
- **`app/api/`**: Contains all API-related files:
  - **`auth.py`**: Manages user authentication endpoints such as registration and login.
  - **`bookings.py`**: Handles booking-related endpoints for seat reservations.
  - **`trains.py`**: Manages train-related endpoints for adding and viewing trains.
- **`app/services/`**: Contains business logic services:
  - **`auth_service.py`**: Contains logic for user registration and login.
  - **`booking_service.py`**: Handles the logic for booking tickets and checking seat availability.
- **`app/database.py`**: Contains the logic for establishing a connection to the PostgreSQL database.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`run.py`**: The entry point to run the Flask application.

