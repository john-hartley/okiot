from sqlmodel import Field, SQLModel

class PolicyHolder(SQLModel, table=True):
    __tablename__ = "policy_holder"

    id: int = Field(primary_key=True)
    first_name: str
    last_name: str