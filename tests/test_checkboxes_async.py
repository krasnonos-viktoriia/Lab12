import pytest
import allure
from pages.checkboxes_page import CheckboxesPage


@pytest.mark.asyncio
@allure.title("Checkbox test with Allure steps and screenshot")
async def test_checkboxes_with_steps(page):
    checkboxes = CheckboxesPage(page)

    with allure.step("Open checkboxes page"):
        await checkboxes.open()

    with allure.step("Check first checkbox"):
        await checkboxes.check_first_checkbox()
        assert await checkboxes.is_first_checked()

    with allure.step("Uncheck second checkbox"):
        await checkboxes.uncheck_second_checkbox()
        assert not await checkboxes.is_second_checked()

    with allure.step("Attach screenshot of checkboxes"):
        screenshot = await page.screenshot(path="screenshots/checkboxes_attachment.png")

        allure.attach(
            screenshot,
            name="checkboxes_attachment",
            attachment_type=allure.attachment_type.PNG
        )