class AlertsPage:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, page):
        self.page = page
        self.alert_button = page.locator("button[onclick='jsAlert()']")
        self.confirm_button = page.locator("button[onclick='jsConfirm()']")
        self.result = page.locator("#result")

    async def open(self):
        await self.page.goto(self.URL)

    async def click_alert_button(self):
        await self.alert_button.click()

    async def click_confirm_button(self):
        await self.confirm_button.click()

    async def get_result_text(self):
        return await self.result.text_content()