from dataclasses import dataclass
from datetime import datetime

from responses.policyHolderResponse import PolicyHolderResponse

@dataclass
class PolicyResponse:
    id: int
    policyHolder: PolicyHolderResponse
    type: str
    startsAt: datetime
    endsAt: datetime
    autoRenews: bool