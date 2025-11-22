# Github Actions Demo - FastAPI CI/CD

This is a simple FastAPI project created to learn GitHub Actions (CI/CD).

## 🚀 Features
- FastAPI server with `/health` and `/sum` endpoints
- Pytest for unit testing
- GitHub Actions CI (test automation)

---

## 📂 Project Structure
```
Githubactions-demo/
│
├── app/
│   ├── __init__.py
│   └── main.py                # FastAPI application file
│
├── tests/
│   └── test_main.py           # Pytest test cases
│
├── .github/
│   └── workflows/
│       └── python-ci.yml      # GitHub Actions CI workflow
│
├── render.yaml               # Render deployment configuration
├── requirements.txt          # Python dependencies
├── pytest.ini                # Pytest config (to fix module import issues)
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── venv/                     # Virtual environment (ignored by Git)
```