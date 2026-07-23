# PROTOCOL.md

# Urja Meter Operations Portal – Protocol Documentation

## Overview

This document describes the authentication process and internal API endpoints discovered while reverse engineering the Urja Meter Operations Portal using the browser's Developer Tools (Network tab).

---

# Base URL

```
https://urja-ops.flockenergy.tech
```

---

# Authentication

## Endpoint

```
POST /login
```

## Request Headers

```http
Content-Type: application/x-www-form-urlencoded
Origin: https://urja-ops.flockenergy.tech
Referer: https://urja-ops.flockenergy.tech/login
X-SvelteKit-Action: true
```

## Request Body

| Parameter | Type | Description |
|----------|------|-------------|
| email | String | Operator email |
| password | String | Operator password |

Example

```text
email=operator@urja.local
password=urja-ops-2026
```

---

## Response

```
HTTP 200 OK
```

Returns a redirect response:

```json
{
    "type": "redirect",
    "status": 303,
    "location": "/meters"
}
```

The server also sets the following authentication cookie:

```
__Secure-better-auth.session_token
```

This session cookie is required for accessing all protected endpoints.

---

# Meter Search

## Endpoint

```
GET /portal/meters/search?q=&page=1
```

## Description

Returns a paginated list of registered electricity meters.

## Sample Response

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
    ],
    "page": 1,
    "pageSize": 20,
    "total": 403
}
```

---

# Energy Data

## Endpoint

```
GET /portal/meters/{meter_id}/energy
```

## Description

Returns interval-wise energy consumption information for the specified meter.

## Sample Response

```json
{
    "data": [
        {
            "timestamp": "23/06/2026 23:30",
            "kwh": "48438.74",
            "kvah": "52313.84",
            "voltR": "226"
        }
    ]
}
```

---

# Geolocation

## Endpoint

```
GET /portal/meters/{meter_id}/geo
```

## Description

Returns the geographical coordinates of the selected meter.

## Sample Response

```json
{
    "data": {
        "latitude": "26.93896",
        "longitude": "75.83095"
    }
}
```

---

# Session Management

- Authentication is performed once using the login endpoint.
- The application stores the returned session cookie.
- All subsequent API requests reuse the same authenticated session.
- No additional login requests are required until the session expires.

---

# Reverse Engineering Notes

The API endpoints were identified using Chrome Developer Tools by inspecting the Network tab during user interactions with the portal.

The following information was captured:

- Login request
- Required request headers
- Session cookie
- Meter search endpoint
- Energy endpoint
- Geolocation endpoint

The FastAPI wrapper replicates these browser requests using an authenticated `httpx.Client`, allowing secure access to the portal's internal APIs.