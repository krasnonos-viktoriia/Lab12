class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    async def open(self):
        await self.page.goto(self.URL)

    async def login(self, username, password):
        await self.username.fill(username)
        await self.password.fill(password)
        await self.login_button.click()

    async def get_message(self):
        return await self.flash_message.text_content()