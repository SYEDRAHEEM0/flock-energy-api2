# REFLECTION.md

# Project Reflection

## Overview

The objective of this assignment was to reverse engineer the Urja Meter Operations Portal and develop a FastAPI-based API wrapper that provides simplified REST endpoints for accessing meter information, energy consumption, and geolocation data.

The project involved understanding the portal's authentication mechanism, maintaining an authenticated session, and exposing clean APIs that abstract the complexity of the underlying web application.

---

# Development Approach

The implementation was completed in the following stages:

1. Inspected the Urja portal using Chrome Developer Tools.
2. Identified the login endpoint and required request headers.
3. Captured the authentication cookie generated after successful login.
4. Discovered the internal APIs used by the portal.
5. Implemented an authenticated HTTP client using `httpx.Client`.
6. Built FastAPI endpoints that reuse the authenticated session.
7. Tested the APIs using both a standalone client script and FastAPI Swagger UI.

---

# Challenges Faced

## Authentication

The biggest challenge was replicating the browser's login request.

Initially, every login attempt resulted in:

```
403 Cross-site POST form submissions are forbidden
```

This occurred because the browser was sending additional headers and maintaining session state that were not included in the initial implementation.

---

## Session Management

After successful authentication, the server returned a secure session cookie.

Instead of logging in before every request, the application was modified to maintain a persistent authenticated `httpx.Client`, allowing all API requests to reuse the same session.

---

## Reverse Engineering

The portal does not provide public API documentation.

Therefore, all endpoints, request headers, request payloads, and response formats had to be identified manually by inspecting browser network traffic using Chrome Developer Tools.

---

# Assumptions

- The authentication credentials remain valid throughout execution.
- The session cookie remains active until it expires.
- The internal API endpoints remain unchanged.
- Responses are returned in JSON format.

---

# Design Decisions

- Used **FastAPI** because of its simplicity, performance, and automatic API documentation.
- Used **httpx.Client** to maintain persistent HTTP sessions.
- Stored configuration values in environment variables using **Pydantic Settings**.
- Kept authentication logic inside a dedicated client class to separate networking logic from API endpoints.

---

# What Went Well

- Successfully reverse engineered the authentication flow.
- Implemented persistent session handling.
- Exposed clean REST APIs for meter, energy, and geolocation data.
- Verified all endpoints using Swagger UI.
- Generated interactive API documentation automatically through FastAPI.

---

# Possible Improvements

Given additional time, the following improvements could be implemented:

- Better exception handling with custom error responses.
- Automatic session renewal when authentication expires.
- Request and response logging.
- Unit and integration tests.
- Pagination support for meter listings.
- Docker support for simplified deployment.
- Caching frequently requested data.
- CI/CD pipeline for automated testing and deployment.

---

# Learning Outcomes

This project provided practical experience in:

- Reverse engineering web applications.
- HTTP authentication and session management.
- Cookie-based authentication.
- Building REST APIs using FastAPI.
- Using Chrome Developer Tools for API discovery.
- Designing reusable backend components.
- Exposing internal services through a clean API interface.

---

# Conclusion

The project successfully demonstrates how an authenticated web application can be reverse engineered and wrapped with a modern REST API. The final solution authenticates with the Urja Meter Operations Portal, maintains an active session, and exposes simplified endpoints for retrieving meter information, energy consumption, and geolocation data through FastAPI.