import allure


@allure.title("Перевірка головної сторінки")
def test_home_page(page):
    page.goto("https://the-internet.herokuapp.com")

    title = page.title()
    assert title == "The Internet"

    assert page.url == "https://the-internet.herokuapp.com/"

    text = page.locator("h1").text_content()
    assert "Welcome to the-internet" in text

    page.screenshot(path="screenshots/home_page.png")