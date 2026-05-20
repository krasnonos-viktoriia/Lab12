import allure


@allure.title("Перевірка JavaScript alert")
def test_alert_accept(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    dialog_text = []

    def handle_dialog(dialog):
        dialog_text.append(dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.click("button[onclick='jsAlert()']")

    result = page.locator("#result").text_content()

    assert dialog_text[0] == "I am a JS Alert"
    assert result == "You successfully clicked an alert"

@allure.title("Перевірка JavaScript confirm з Cancel")
def test_confirm_dismiss(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    dialog_text = []

    def handle_dialog(dialog):
        dialog_text.append(dialog.message)
        dialog.dismiss()

    page.on("dialog", handle_dialog)

    page.click("button[onclick='jsConfirm()']")

    result = page.locator("#result").text_content()

    assert dialog_text[0] == "I am a JS Confirm"
    assert result == "You clicked: Cancel"