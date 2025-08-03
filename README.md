---
# 💸 Finance Tracker

Finance Tracker is a modern web app for managing your personal finances. Built with FastAPI, Jinja2, and SQLite, it lets you track expenses, set your income, and view your financial summary in a beautiful dashboard. Easily add, categorize, and delete transactions, and see your total income, expenses, and balance at a glance.

---

## ✨ Features

- Add and categorize expenses
- Set and update your total income
- View all transactions in a stylish dashboard
- See summary cards for income, expenses, and balance
- Delete transactions instantly
- Responsive, professional UI with cards and color accents
- Data stored locally in SQLite (`instance/finance.db`)

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/finance-tracker.git
   cd finance-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   uvicorn src.app:app --reload
   ```

5. **Open in your browser**
   ```
   http://127.0.0.1:8000
   ```

---

## 🗂️ Project Structure

```
finance-tracker/
├── src/
│   ├── app.py                 # FastAPI app entry point
│   ├── models.py              # SQLAlchemy models
│   ├── forms.py               # Form handling logic
│
├── templates/                 # HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── add_transaction.html
│   └── set_income.html
│
├── static/                    # CSS and assets
│   └── style.css
│
├── instance/                  # SQLite database & income config
│   ├── finance.db
│   └── income.txt
│
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignore rules
├── README.md                  # This file
```

---

## 🧠 Tech Stack

- FastAPI
- Jinja2
- SQLAlchemy
- SQLite
- HTML/CSS

---

## 📌 Usage Notes

- Add expenses via `/add`
- Set or update your income via `/set-income`
- View and delete transactions on `/`
- All data is stored locally in `instance/finance.db` and `instance/income.txt`

---

## 📜 License

MIT License

##🔗 **Live Demo**:

[https://my-finance-tracker-sk1t.onrender.com](https://my-finance-tracker-sk1t.onrender.com)

