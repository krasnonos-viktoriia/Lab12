import allure

@allure.title("Логін з неправильним паролем")
def test_invalid_password(page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "wrong_password")
    page.click("button[type='submit']")

    message = page.locator("#flash").text_content()

    assert "Your password is invalid!" in message

    page.screenshot(path="screenshots/invalid_password.png")