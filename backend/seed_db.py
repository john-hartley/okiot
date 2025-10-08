from datetime import datetime
from sqlmodel import SQLModel, Session, create_engine

from models.policy import Policy
from models.policyHolder import PolicyHolder

engine = create_engine("sqlite:///insurance.db", echo=True)
SQLModel.metadata.create_all(engine)

policy_holder_1 = PolicyHolder(id=1, first_name="Bob", last_name="Builder")
policy_holder_2 = PolicyHolder(id=2, first_name="Benny", last_name="Boiler")
policy_holder_3 = PolicyHolder(id=3, first_name="Bugs", last_name="Bunny")

policy_1 = Policy(
    id=1,
    policy_holder_id=1,
    type="Indemnity",
    starts_at=datetime.strptime("2025-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    ends_at=datetime.strptime("2026-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    auto_renews=True
)

policy_2 = Policy(
    id=2,
    policy_holder_id=2,
    type="Home",
    starts_at=datetime.strptime("2025-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    ends_at=datetime.strptime("2027-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    auto_renews=False
)

policy_3 = Policy(
    id=3,
    policy_holder_id=3,
    type="Carrot",
    starts_at=datetime.strptime("1999-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    ends_at=datetime.strptime("2028-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    auto_renews=False
)

with Session(engine) as session:
    session.add(policy_holder_1)
    session.add(policy_holder_2)
    session.add(policy_holder_3)
    session.add(policy_1)
    session.add(policy_2)
    session.add(policy_3)
    session.commit()