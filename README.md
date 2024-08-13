# Pirates E-learning Platform

Pirates is a modern E-learning platform built with Django. It provides a user-friendly interface for browsing courses, Sign-in and login in,enrolling to courses and accessing course content, and a chat server to allow students chat with course moderators.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Pirates is a platform where users can:
- Browse courses from different range of displayed courses
- Sign-up and log in*
- Enroll to courses.
- Access to enrolled courses
- Currently building a chat server to allow users to communicate with the course moderators*

## Features

- User Authentication (Sign Up, Login, Logout)
- User friendly interface
- Different range of courses
- A chat server 
- A content management sytem 
- Restfull Api

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/dackMatta/e-learning
    cd e-learning
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. **Browse Courses**: Browse through courses displayed on the landing page.

2. **Sign-up or Log-in**: Enroll to courses by either creating an account or log-in.
3. **Access course content**: A display of courses one has enrolled for.
4. **Message your moderators**: Directly message your moderators for consultation .
5. **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

Please ensure your code follows our coding standards and includes relevant tests.
Front-end developers help build a user friendly interface

## License

Working on it!.