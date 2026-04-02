# API de Login con FastAPI + SQLModel

## Descripción
API REST mínima que implementa un endpoint de login contra una base de datos embebida (quemada en código) usando SQLModel.

## Requisitos
- Python 3.10+
- SQLModel
- FastAPI

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
```bash
fastapi dev main.py
```

## Ejemplos de uso

**Login exitoso:**
- URL: http://localhost:8000/docs
- Endpoint: POST /login
- Body:
```json
{
  "username": "admin",
  "password": "admin"
}
```
- Respuesta: `{"message": "Login successful"}`

**Login fallido:**
```json
{
  "username": "admin",
  "password": "wrongpassword"
}
```
- Respuesta: `{"message": "Invalid username or password"}`

## Usuarios de ejemplo
| Username | Password |
|----------|----------|
| admin    | admin    |
| user     | user     |
| guest    | guest    |
