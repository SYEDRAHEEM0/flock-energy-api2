# Flock Energy API Wrapper

## Overview

The **Flock Energy API Wrapper** is a FastAPI-based backend service that authenticates with the Urja Meter Operations Portal and exposes simplified REST APIs for retrieving meter information, energy consumption, and geolocation data.

The application maintains an authenticated session with the Urja portal, eliminating the need for clients to handle login, cookies, or session management.

---

## Features

- Secure authentication with the Urja Meter Portal
- Persistent session management using HTTP cookies
- Retrieve the list of available meters
- Retrieve energy consumption data for a specific meter
- Retrieve geolocation details for a specific meter
- Interactive API documentation using Swagger UI

---

## Technology Stack

- Python 3.12
- FastAPI
- HTTPX
- Pydantic Settings
- Uvicorn

---

## Project Structure

```
flock-energy-api/
│
├── app/
│   ├── client.py
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
├── test_client.py
├── README.md
├── PROTOCOL.md
├── REFLECTION.md
└── openapi.json
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd flock-energy-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root.

```env
BASE_URL=https://urja-ops.flockenergy.tech
EMAIL=operator@urja.local
PASSWORD=urja-ops-2026
```

---

## Running the Application

Start the FastAPI development server.

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

OpenAPI Specification

```
http://127.0.0.1:8000/openapi.json
```

---

## Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health check |
| GET | `/meters` | Retrieve available meters |
| GET | `/meters/{meter_id}/energy` | Retrieve energy consumption |
| GET | `/meters/{meter_id}/geo` | Retrieve geolocation |

---

## Authentication

The application authenticates with the Urja Meter Portal using the configured credentials and maintains the session internally using the `__Secure-better-auth.session_token` cookie. Clients consuming this API are not required to manage authentication.

---

## Example Response

### GET /meters

```json
{
  "data": [
    {
      "meterId": "J100000",
      "serialNo": "SE33962",
      "make": "HPL",
      "phaseType": "single",
      "installStatus": "Decommissioned",
      "dtCode": "DT-001"
    }
  ]
}
```

---

## Future Improvements

- Add pagination support
- Improved exception handling
- Request logging
- Unit and integration tests
- Docker containerization

---

## Author

**Syed Raheem**