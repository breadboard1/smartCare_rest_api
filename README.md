# SmartCare Hospital Project

SmartCare Hospital is a Django-based application built to provide comprehensive healthcare services through an easy-to-use REST API. With SmartCare, patients can create accounts, view doctor information, book online or offline appointments, and leave reviews for doctors and the hospital.

## Table of Contents

- [SmartCare Hospital Project](#smartcare-hospital-project)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Built With](#built-with)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)

## About the Project

SmartCare is designed to streamline patient interactions with hospital services. By leveraging the Django REST framework, we’ve built an API system to make healthcare information easily accessible. Patients can create accounts, book appointments, and leave reviews with ease.

## Built With

- **Python**
- **Django**
- **Django REST Framework**

## Features

- **Account Management**: Patients can register, log in, and log out.
- **Doctor Information**: Patients can view detailed information about doctors.
- **Appointment Booking**: Patients can book appointments both online and offline.
- **Reviews**: Patients can leave reviews for both doctors and the hospital.

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/breadboard1/SmartCareHospital.git
    ```

2. Navigate to the project directory:
    ```bash
    cd SmartCareHospital
    ```

3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Account Management**: Register, log in, and log out to manage your profile.
2. **Doctor Info**: View the list of available doctors and their details.
3. **Appointments**: Book appointments either online or offline.
4. **Reviews**: Leave reviews for doctors and the hospital.
