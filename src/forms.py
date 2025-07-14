from pydantic import BaseModel

class TransactionForm(BaseModel):
    amount: float
    category: str
    description: str = ""
