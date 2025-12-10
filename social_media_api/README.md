# Social Media API - User Authentication

## Setup

1. Clone repo and create virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run server: `python manage.py runserver`

## API Endpoints

- POST `/api/accounts/register/` → register user, returns token
- POST `/api/accounts/login/` → login user, returns token
- GET `/api/accounts/profile/` → get logged-in user profile, requires token

## User Model

Fields: username, email, password, bio, profile_picture, followers
