import pytest
import allure
from pages.login_page import LoginPage


@pytest.mark.asyncio
@allure.title("Successful login with Allure steps and screenshot")
async def test_login_with_steps(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        await login.open()

    with allure.step("Enter valid username and password"):
        await login.login("tomsmith", "SuperSecretPassword!")

    with allure.step("Verify success message"):
        message = await login.get_message()
        assert "You logged into a secure area!" in message

    with allure.step("Attach screenshot after login"):
        screenshot = await page.screenshot(path="screenshots/login_attachment.png")

        allure.attach(
            screenshot,
            name="login_attachment",
            attachment_type=allure.attachment_type.PNG
        )