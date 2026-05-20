import pytest
import allure


@pytest.mark.asyncio
@allure.title("New window test with screenshot attachment")
async def test_new_window_with_screenshot(page):
    with allure.step("Open windows page"):
        await page.goto("https://the-internet.herokuapp.com/windows")

    with allure.step("Click link and open new window"):
        async with page.context.expect_page() as page_event:
            await page.locator("a[href='/windows/new']").click()

        new_page = await page_event.value
        await new_page.wait_for_load_state()

    with allure.step("Verify new window title and URL"):
        title = await new_page.title()
        assert "New Window" in title
        assert new_page.url == "https://the-internet.herokuapp.com/windows/new"

    with allure.step("Attach screenshot of new window"):
        screenshot = await new_page.screenshot(path="screenshots/new_window_attachment.png")

        allure.attach(
            screenshot,
            name="new_window_attachment",
            attachment_type=allure.attachment_type.PNG
        )

    await new_page.close()