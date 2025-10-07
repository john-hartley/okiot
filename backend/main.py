from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

policies = {
    1: {
        "id": 1,
        "policyHolder": {
            "firstName": "Bob",
            "lastName": "Builder"
        },
        "type": "indemnity",
        "startsAt": "2025-01-01 00:00:00",
        "endsAt": "2026-01-01 00:00:00",
        "autoRenews": False
    },
    2: {
        "id": 2,
        "policyHolder": {
            "firstName": "Benny",
            "lastName": "Boiler"
        },
        "type": "home",
        "startsAt": "2025-01-01 00:00:00",
        "endsAt": "2027-01-01 00:00:00",
        "autoRenews": True
    },
    3: {
        "id": 3,
        "policyHolder": {
            "firstName": "Bugs",
            "lastName": "Bunny"
        },
        "type": "carrot",
        "startsAt": "1999-01-01 00:00:00",
        "endsAt": "2028-01-01 00:00:00",
        "autoRenews": True
    }
}

@app.get("/policies/{id}")
def get_policy(id: int):
    if id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found")

    return policies[id]