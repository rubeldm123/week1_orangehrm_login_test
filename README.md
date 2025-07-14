
# 🧪 Week 1: OrangeHRM Login Test Using Playwright and Pytest

This project is part of a full QA Automation Engineer learning path using Playwright with Python.

In **Week 1**, you’ll automate the login functionality of the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using Playwright and Pytest in asynchronous mode.

---

## ✅ What You'll Learn

- How to set up a Python project with virtual environment (venv)
- How to install and configure Playwright with Pytest
- How to write your first async UI automation test
- How to use reusable browser fixtures with `conftest.py`
- How to structure your first automation test project

---

## 📁 Project Structure

```

week1_orangehrm_login_test/ 
├── venv/                        # Python virtual environment (ignored in Git)
├── tests/
│   └── test_orangehrm_login.py  # Main test case for OrangeHRM login
├── conftest.py                 # Pytest fixture for Playwright page object
├── requirements.txt            # All required packages
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation (this file)

````

---

## ⚙️ Step-by-Step Setup

### 1️⃣ Create Project Folder

```bash
mkdir week1_orangehrm_login_test
cd week1_orangehrm_login_test
````

---

### 2️⃣ Create and Activate Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Create `requirements.txt`

```txt
pytest==7.2.0
pytest-playwright==0.6.2
playwright==1.44.0
pytest-asyncio==0.20.3
```

Then install all dependencies:

```bash
pip install -r requirements.txt
python -m playwright install
```

---

### 4️⃣ Create `.gitignore`

```txt
venv/
__pycache__/
*.pyc
allure-results/
```

---

### 5️⃣ Create Folder and Files

```bash
mkdir tests
touch conftest.py
touch tests/test_orangehrm_login.py
```

---

### 6️⃣ Add the Code

#### 🔹 `conftest.py`

```python
import pytest_asyncio
from playwright.async_api import async_playwright

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()
```

#### 🔹 `tests/test_orangehrm_login.py`

```python
import pytest

@pytest.mark.asyncio
async def test_orangehrm_login(page):
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await page.fill("input[name='username']", "Admin")
    await page.fill("input[name='password']", "admin123")
    await page.click("button[type='submit']")
    await page.wait_for_selector("h6:has-text('Dashboard')")
    assert await page.is_visible("h6:has-text('Dashboard')")
```

---

## ▶️ How to Run the Test

```bash
pytest tests/test_orangehrm_login.py -s -v
```

You should see a Chromium browser open, log in using credentials, and validate that the dashboard is visible.

---

## 🔐 Credentials Used

* **Username:** `Admin`
* **Password:** `admin123`
* **Login URL:** [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## 📤 How to Upload This Project to GitHub (First Time)

### 1️⃣ Create a new repository on GitHub

* Go to [https://github.com](https://github.com)
* Click “New”
* Name the repo: `week1_orangehrm_login_test`
* Leave README, .gitignore, and license **unchecked**
* Click “Create repository”

### 2️⃣ Initialize Git in the local project

```bash
git init
git add .
git commit -m "Initial commit - OrangeHRM login test"
```

### 3️⃣ Add your GitHub repository (replace with your GitHub username)

```bash
git remote add origin https://github.com/yourusername/week1_orangehrm_login_test.git
git branch -M main
git push -u origin main
```

✅ Done! Visit:
`https://github.com/yourusername/week1_orangehrm_login_test`





```
