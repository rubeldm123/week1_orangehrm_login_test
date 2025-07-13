import pytest

@pytest.mark.asyncio
async def test_orangehrm_login(page):
    # Step 1: Go to OrangeHRM login page
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Fill in username and password
    await page.fill("input[name='username']", "Admin")
    await page.fill("input[name='password']", "admin123")

    # Step 3: Click the login button
    await page.click("button[type='submit']")

    # Step 4: Wait for dashboard heading to appear
    await page.wait_for_selector("h6:has-text('Dashboard')")

    # Step 5: Verify dashboard is visible
    assert await page.is_visible("h6:has-text('Dashboard')")
