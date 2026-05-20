import pytest
import allure
from pages.alerts_page import AlertsPage


@pytest.mark.asyncio
@allure.title("JavaScript alert test with Allure steps")
async def test_alert_with_steps(page):
    alerts = AlertsPage(page)
    dialog_text = []

    with allure.step("Open alerts page"):
        await alerts.open()

    async def handle_dialog(dialog):
        dialog_text.append(dialog.message)

        allure.attach(
            dialog.message,
            name="alert_text",
            attachment_type=allure.attachment_type.TEXT
        )

        await dialog.accept()

    with allure.step("Register dialog handler"):
        page.on("dialog", handle_dialog)

    with allure.step("Click alert button"):
        await alerts.click_alert_button()

    with allure.step("Verify result message"):
        result = await alerts.get_result_text()

        assert dialog_text[0] == "I am a JS Alert"
        assert result == "You successfully clicked an alert"