import os
import allure


@allure.title("Перевірка створення скріншотів після логіну та нової вкладки")
def test_screenshots_login_and_new_window(page):
    # Крок 2: створення окремої папки screenshots
    os.makedirs("screenshots", exist_ok=True)

    # Крок 1: screenshot після логіну
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    message = page.locator("#flash").text_content()
    assert "You logged into a secure area!" in message

    page.screenshot(path="screenshots/after_login.png")

    # Крок 3: screenshot нової вкладки
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.context.expect_page() as page_event:
        page.locator("a[href='/windows/new']").click()

    new_page = page_event.value
    new_page.wait_for_load_state()

    assert "New Window" in new_page.title()
    assert new_page.url == "https://the-internet.herokuapp.com/windows/new"

    new_page.screenshot(path="screenshots/new_window.png")

    new_page.close()