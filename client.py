import httpx
from app.config import settings


class UrjaPortalClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url=settings.BASE_URL,
            follow_redirects=True,
            timeout=20.0,
        )
        self.logged_in = False

    def login(self):
        # Visit login page first
        self.client.get("/login")

        response = self.client.post(
            "/login",
            data={
                "email": settings.EMAIL,
                "password": settings.PASSWORD,
            },
            headers={
                "Origin": settings.BASE_URL,
                "Referer": f"{settings.BASE_URL}/login",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-SvelteKit-Action": "true",
            },
        )

        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        print("COOKIES:", self.client.cookies)

        if "__Secure-better-auth.session_token" in self.client.cookies:
            self.logged_in = True
            print("✅ Login Success")
            return True

        raise Exception("Login Failed")

    def ensure_login(self):
        if not self.logged_in:
            self.login()

    def get_meters(self, q="", page=1):
        self.ensure_login()

        response = self.client.get(
            "/portal/meters/search",
            params={
                "q": q,
                "page": page,
            },
        )

        response.raise_for_status()
        return response.json()

    def get_energy(self, meter_id):
        self.ensure_login()

        response = self.client.get(
            f"/portal/meters/{meter_id}/energy"
        )

        response.raise_for_status()
        return response.json()

    def get_geo(self, meter_id):
        self.ensure_login()

        response = self.client.get(
            f"/portal/meters/{meter_id}/geo"
        )

        response.raise_for_status()
        return response.json()