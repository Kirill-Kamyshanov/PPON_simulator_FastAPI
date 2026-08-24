from pydantic import BaseModel

class GetBalance(BaseModel):
    amount: int