# 🌙 Late Show API

A Flask-based REST API for managing late-night show guests, episodes, and appearances, built with PostgreSQL and secured with JWT authentication.

---

## 📦 Tech Stack

- Python 3.8+
- Flask + Flask-SQLAlchemy + Flask-Migrate
- PostgreSQL
- Flask-JWT-Extended (token-based authentication)
- Pipenv
- Postman (for API testing)

---

## 🛠 Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
pipenv install
pipenv shell
2. Create PostgreSQL Database
Open psql and run:

sql
Copy
Edit
CREATE DATABASE lateshow_db;
3. Configure Environment
In .env:

env
Copy
Edit
DATABASE_URL=postgresql://<your_username>:<your_password>@localhost/lateshow_db
JWT_SECRET_KEY=supersecret
Then in server/config.py, reference it:

python
Copy
Edit
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
🚀 Run the App
1. Initialize and Migrate DB
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
2. Seed Sample Data
bash
Copy
Edit
python -m server.seed
3. Start the Server
bash
Copy
Edit
flask run
🔐 Auth Flow (JWT)
✅ Register
h
Copy
Edit
POST /auth/register
Content-Type: application/json

{
  "username": "fahiye",
  "password": "password123"
}
✅ Login
h
Copy
Edit
POST /auth/login
Content-Type: application/json

{
  "username": "fahiye",
  "password": "password123"
}
Response:

json
Copy
Edit
{
  "access_token": "your.jwt.token"
}
Use this token in the header for protected routes:

makefile
Copy
Edit
Authorization: Bearer your.jwt.token
📚 Routes Overview
Method	Endpoint	Auth Required	Description
POST	/auth/register	❌	Register new user
POST	/auth/login	❌	Login and get token
GET	/guests	❌	List all guests
GET	/episodes	❌	List all episodes
GET	/episodes/:id	❌	Get one episode with appearances
DELETE	/episodes/:id	✅	Delete episode + appearances
POST	/appearances	✅	Add a guest appearance to episode

📬 Sample Request & Response
GET /episodes/1
Response:

json
Copy
Edit
{
  "id": 1,
  "date": "2025-06-20",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "guest_id": 1,
      "guest_name": "John Doe",
      "rating": 5
    }
  ]
}
 Postman Usage
Import the included file: challenge-4-lateshow.postman_collection.json

Use /auth/login to get your token

For protected routes, add:

http
Copy
Edit
Authorization: Bearer your.jwt.token
to the Headers tab of your requests.

🔗 GitHub Repo
GitHub https://github.com/fahiyemuhammad/late-show-api-challenge.git
```
