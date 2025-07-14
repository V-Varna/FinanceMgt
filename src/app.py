from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from src.models import Base, Transaction, get_db, engine
from src.forms import TransactionForm
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Create DB tables if not exist
Base.metadata.create_all(bind=engine)

# Store income in a simple config file (or you can use DB)
INCOME_FILE = "instance/income.txt"

def get_income():
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r") as f:
            try:
                return float(f.read().strip())
            except Exception:
                return 0.0
    return 0.0
@app.post("/delete/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
    return RedirectResponse("/", status_code=303)

def set_income(value: float):
    with open(INCOME_FILE, "w") as f:
        f.write(str(value))

@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).order_by(Transaction.date.desc()).all()
    total_income = get_income()
    total_expense = sum(-t.amount for t in transactions if t.amount < 0)
    balance = total_income - total_expense
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "transactions": transactions,
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance
        }
    )

@app.get("/add")
def add_transaction_form(request: Request):
    return templates.TemplateResponse("add_transaction.html", {"request": request})

@app.post("/add")
def add_transaction(request: Request, amount: float = Form(...), category: str = Form(...), description: str = Form(""), db: Session = Depends(get_db)):
    # All transactions are expenses (negative amounts)
    form = TransactionForm(amount=-abs(amount), category=category, description=description)
    db.add(Transaction(**form.dict()))
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/set-income")
def set_income_form(request: Request):
    return templates.TemplateResponse("set_income.html", {"request": request, "current_income": get_income()})

@app.post("/set-income")
def set_income_post(request: Request, income: float = Form(...)):
    set_income(income)
    return RedirectResponse("/", status_code=303)
