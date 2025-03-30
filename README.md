# Discount Campaign App

A mini shopping cart (Fixed Items) app that lets users apply discount campaigns via FastAPI + JS UI.

## Features

- Select one discount per category
- Apply multiple categories in order (Coupon > On Top > Seasonal)
- Shows total before/after discount

## How to Run

### 1. Install Requirements

Use a virtual environment (recommended):

```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
```

### 2. Run Backend FastAPI

@Terminal 1

```bash
cd app
uvicorn main:app --reload --port 8000
```

### 3. Run Frontend UI

@Terminal 2

```bash
cd ui
python3 -m http.server 5050
```

### 4. Apply Discount Campaign

Visit the frontend in your browser: http://localhost:5050


## Author

**Pattadon Thepkan**
