
```markdown
# 🧪 Week 1: OrangeHRM Login Test Using Playwright and Pytest

This project is part of a complete QA Automation Engineer portfolio using Playwright with Python.  
In Week 1, we automate a simple login test using the [OrangeHRM Demo Website](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) with Playwright + Pytest in async mode.

---

## ✅ What You'll Learn

- How to set up a Python project with virtual environment (venv)
- How to install and configure Playwright with Pytest
- How to write your first async UI automation test
- How to use fixtures in `conftest.py`
- How to structure your first automation project

---

## 📁 Project Structure

```

week1\_orangehrm\_login\_test/
├── venv/                          # Python virtual environment (ignored in Git)
├── tests/
│   └── test\_orangehrm\_login.py    # Main test file
├── conftest.py                    # Pytest fixture for Playwright page
├── requirements.txt               # All required packages
├── .gitignore                     # Files/folders to ignore in Git
└── README.md                      # This documentation file

````

---

## ⚙️ Step-by-Step Setup

### 1️⃣ Create Project Directory

```bash
mkdir week1_orangehrm_login_test
cd week1_orangehrm_login_test
````

---

### 2️⃣ Create and Activate Virtual Environment

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Create `requirements.txt`

Paste the following:

```txt
pytest==7.2.0
pytest-playwright==0.6.2
playwright==1.44.0
pytest-asyncio==0.20.3
```

Then install:

```bash
pip install -r requirements.txt
python -m playwright install
```

---

### 4️⃣ Create `.gitignore`

```
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

### 6️⃣ Add Code

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
    # Step 1: Open login page
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Enter username and password
    await page.fill("input[name='username']", "Admin")
    await page.fill("input[name='password']", "admin123")

    # Step 3: Click login button
    await page.click("button[type='submit']")

    # Step 4: Wait for Dashboard heading
    await page.wait_for_selector("h6:has-text('Dashboard')")

    # Step 5: Verify Dashboard is visible
    assert await page.is_visible("h6:has-text('Dashboard')")
```

---

## ▶️ How to Run the Test

```bash
pytest tests/test_orangehrm_login.py -s -v
```

✅ You’ll see the browser open, fill in credentials, and verify login was successful.

---

## ✅ Login Credentials Used

* **Username:** `Admin`
* **Password:** `admin123`
* **URL:** `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`

---

## 🧠 Summary

| Concept             | Why It’s Important                         |
| ------------------- | ------------------------------------------ |
| Virtual Environment | Isolates project dependencies              |
| Playwright          | Automates browser interactions             |
| Pytest              | Lightweight test runner                    |
| Async/Await         | Handles browser timing & waits effectively |
| Fixtures            | Reuse setup code across tests              |
| Git Ignore          | Keeps repo clean and professional          |

---

## 🚀 Next Step (Week 2)

✅ Convert this into a Page Object Model (POM) framework
✅ Add JSON-based test data
✅ Add screenshots on failure
✅ Integrate Allure reports and Docker for CI


