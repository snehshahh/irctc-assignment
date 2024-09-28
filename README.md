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

### Environment Variables Setup

To ensure the security of the database and API keys, you need to set up environment variables. Follow these steps:

1. **Create a new file** named `.env` in the root folder(same folder where the app.py is there) of the project.
2. **Add the following environment variables** to the `.env` file:

FOR EG:

    JWT_SECRET_KEY=c1af7e8a0fc82c0d487ef1a08443eb8762e92f5a22c9662403d788b6ab490cbf
    ADMIN_API_KEY=08ad77dd3c6c0d36613a0be3e896a7166305c49a1ca6c4f0ce965ee2b8bec8f7
    HOST=localhost
    DATABASE=IRCTC
    USER=postgres
    PASSWORD=admin

### Database Setup
To set up the PostgreSQL database for this project, use the following `CREATE TABLE` queries to create the necessary tables:

    -- Users Table
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(200) NOT NULL,
        email VARCHAR(100) UNIQUE,
        role VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    -- Admin Table
    CREATE TABLE admin_keys (
        admin_key_id SERIAL PRIMARY KEY,
        admin_key VARCHAR(255) NOT NULL,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT admin_keys_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    
    --Trains Table
    CREATE TABLE trains (
        train_id SERIAL PRIMARY KEY,
        train_name VARCHAR(100) NOT NULL,
        source_station VARCHAR(100) NOT NULL,
        destination_station VARCHAR(100) NOT NULL,
        total_seats INTEGER NOT NULL,
        available_seats INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    -- Bookings Table
    CREATE TABLE bookings (
        booking_id UUID NOT NULL,
        user_id INTEGER NOT NULL,
        train_id INTEGER NOT NULL,
        seat_number INTEGER NOT NULL,
        status VARCHAR(10) NOT NULL,
        PRIMARY KEY (booking_id, seat_number),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (train_id) REFERENCES trains(train_id)
    );

## Sample Paramaeters for Testing In Postman
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
       "train_name": "Express Train",
       "source_station": "Station E",
       "destination_station": "Station F",
       "total_seats": 100,
       "api_key": "08ad77dd3c6c0d36613a0be3e896a7166305c49a1ca6c4f0ce965ee2b8bec8f7"
   }'

4. **Train: Get Available Trains**
   Description: Get Available Trains From One Point To Another
   ```bash
   curl -X GET "http://127.0.0.1:5000/trains/get_available_trains?FromStation=Station E&ToStation=Station F"

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

- **`app/config.py`**: Contains configuration settings, including database URLs and secret keys for JWT.
- **`app/models.py`**: Defines data models, including the structure for users, trains, and bookings.
- **`app/api/`**: Contains all API-related files:
  - **`auth.py`**: Manages user authentication endpoints such as registration and login.
  - **`bookings.py`**: Handles booking-related endpoints for seat reservations.
  - **`trains.py`**: Manages train-related endpoints for adding and viewing trains.
- **`app/services/`**: Contains business logic services:
  - **`user_service.py`**: Contains logic for user registration and login.
  - **`train_service.py`**: Contains logic for adding train,Getting Available Tickets etc.
  - **`booking_service.py`**: Handles the logic for booking tickets and checking seat availability.
- **`app/database.py`**: Contains the logic for establishing a connection to the PostgreSQL database.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`app.py`**: The entry point to run the Flask application.

