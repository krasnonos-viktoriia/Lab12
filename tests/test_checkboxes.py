import allure


@allure.title("Перевірка checkbox")
def test_checkboxes(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    checkbox1.check()
    assert checkbox1.is_checked()

    checkbox2.uncheck()
    assert not checkbox2.is_checked()

    page.screenshot(path="screenshots/checkboxes.png")