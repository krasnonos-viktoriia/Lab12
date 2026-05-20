import allure


@allure.title("Перевірка відкриття нової вкладки")
def test_new_window(page):
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.context.expect_page() as page_event:
        page.locator("a[href='/windows/new']").click()

    new_page = page_event.value
    new_page.wait_for_load_state()

    assert "New Window" in new_page.title()
    assert new_page.url == "https://the-internet.herokuapp.com/windows/new"

    new_page.screenshot(path="screenshots/new_window.png")

    new_page.close()

    assert page.url == "https://the-internet.herokuapp.com/windows"

# import allure


# @allure.title("Перевірка відкриття нової вкладки")
# def test_new_window(page):
#     page.goto("https://the-internet.herokuapp.com/windows")

#     with page.context.expect_page() as page_event:
#         page.click("a")

#     new_page = page_event.value
#     new_page.wait_for_load_state()

#     assert "New Window" in new_page.title()
#     assert new_page.url == "https://the-internet.herokuapp.com/windows/new"

#     new_page.screenshot(path="screenshots/new_window.png")

#     new_page.close()

#     assert page.url == "https://the-internet.herokuapp.com/windows"