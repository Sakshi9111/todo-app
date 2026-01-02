# Django Todo Application 📝

A simple, secure, and production-ready Todo application built with Django and Django REST Framework.  
This project follows best practices for code quality, security, and environment-based configuration.

---

## �� Features
- Create, update, and delete todos
- REST API support
- Environment variable–based configuration
- PostgreSQL support
- Secure secret handling
- Docker & Docker Compose support

---

## 🧰 Tech Stack
- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose

---

## ⚙️ How to Run the Application

```bash
git clone https://github.com/Sakshi9111/todo-app.git
cd todo-app

python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows

pip install -r requirements.txt

cp .env.example .env

# Edit .env
# DEBUG=True
# SECRET_KEY=your-secret-key
# ALLOWED_HOSTS=localhost,127.0.0.1
# DB_NAME=todo_db
# DB_USER=todo_user
# DB_PASSWORD=strongpassword
# DB_HOST=localhost
# DB_PORT=5432


# OR run using Docker
docker compose up -d

# Run tests
python manage.py test

