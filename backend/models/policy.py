from sqlmodel import Field, SQLModel
from datetime import datetime

class Policy(SQLModel, table=True):
    id: int = Field(primary_key=True)
    policy_holder_id: int = Field(foreign_key="policy_holder.id")
    type: str
    starts_at: datetime
    ends_at: datetime
    auto_renews: bool