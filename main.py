from fastapi import FastAPI
from app.client import UrjaPortalClient

app = FastAPI(title="Flock Energy API")

client = UrjaPortalClient()


@app.get("/")
def root():
    return {"message": "Flock Energy API is running"}


@app.get("/meters")
def meters(q: str = "", page: int = 1):
    return client.get_meters(q, page)


@app.get("/meters/{meter_id}/energy")
def energy(meter_id: str):
    return client.get_energy(meter_id)


@app.get("/meters/{meter_id}/geo")
def geo(meter_id: str):
    return client.get_geo(meter_id)