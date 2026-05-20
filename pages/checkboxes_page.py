class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page):
        self.page = page
        self.checkbox1 = page.locator("input[type='checkbox']").nth(0)
        self.checkbox2 = page.locator("input[type='checkbox']").nth(1)

    async def open(self):
        await self.page.goto(self.URL)

    async def check_first_checkbox(self):
        await self.checkbox1.check()

    async def uncheck_second_checkbox(self):
        await self.checkbox2.uncheck()

    async def is_first_checked(self):
        return await self.checkbox1.is_checked()

    async def is_second_checked(self):
        return await self.checkbox2.is_checked()