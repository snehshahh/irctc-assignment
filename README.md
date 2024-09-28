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

2. **Make Virtual ENV file**
    ```bash
    python -m venv venv
    source venv/bin/activate 
     # On Windows use:
    venv\Scripts\activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run The App**
   ```bash
   python app.py

### Sample Paramaeters for Testing In Postman
1. **Users: Register**
   Description: Registration Of The User
    ```bash
   curl -X POST http://127.0.0.1:5000/user/register \
   -H "Content-Type: application/json" \
   -d '{
       "username": "Test",
       "password": "Test7634@",
       "email": "Test7634@gmail.com",
       "role": "Admin"
   }'

2. **Users: Login**
    Description: Login User, Getting the Bearer Token In Reponse
    ```bash
   curl -X POST http://127.0.0.1:5000/user/login \
   -H "Content-Type: application/json" \
   -d '{
       "username": "Test",
       "password": "Test7634@",
       "email": "Test7634@gmail.com",
       "role": "Admin"
   }'

3. **Train: Add Trains**
   Description: Adding Train,Assuming the api key is sent in req body, Admins Only
    ```bash
   curl -X POST http://127.0.0.1:5000/trains/add_train \
   -H "Content-Type: application/json" \
   -d '{
       "train_name": "Medium Train",
       "source_station": "Station E",
       "destination_station": "Station F",
       "total_seats": 100,
       "api_key": "c1af7e8a0fc82c0d487ef1a08443eb8762e92f5a22c9662403d788b6ab490cbf"
   }'

4. **Train: Get Available Trains**
   Description: Get Available Trains From One Point To Another
   ```bash
   curl -X GET "http://127.0.0.1:5000/trains/get_available_trains?FromStation=Station A&ToStation=Station B"

5. **Train: Book Ticket**
   Description: Booking Tickets, Assuming there the user to book multiple tickets.
    ```bash
   curl -X POST http://127.0.0.1:5000/bookings/book_ticket \
   -H "Content-Type: application/json" \
   -d '{
       "train_id": 1,
       "no_of_seats_required": 2
   }'

6. **Train: Get Booking Details**
    Description: Get Booking Details On the basis of the Booking Id.
   ```bash
   curl -X GET "http://127.0.0.1:5000/bookings/booking_details?BookingId=35a917d0-528f-4dd7-bf26-942c18d15c03"


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

