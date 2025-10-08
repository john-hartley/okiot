from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, create_engine, select

from models.policy import Policy
from models.policyHolder import PolicyHolder

from responses.policyResponse import PolicyResponse
from responses.policyHolderResponse import PolicyHolderResponse

engine = create_engine("sqlite:///insurance.db", echo=True)
SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

@app.get("/policies/{id}")
def get_policy(id: int):
    with Session(engine) as session:
        statement = select(Policy, PolicyHolder).join(PolicyHolder).where(PolicyHolder.id == id)
        result = session.exec(statement).first()

        if result == None:
            raise HTTPException(status_code=404, detail="Policy not found")

        p, ph = result

        response = PolicyResponse(
            id=p.id,
            policyHolder=PolicyHolderResponse(ph.first_name, ph.last_name),
            type=p.type,
            startsAt=p.starts_at,
            endsAt=p.ends_at,
            autoRenews=p.auto_renews
        )

        return response