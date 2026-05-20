import pytest
import allure


@pytest.mark.asyncio
@allure.title("Демонстрація screenshot при падінні тесту")
async def test_fail_demo(page):
    await page.goto("https://the-internet.herokuapp.com")

    assert await page.title() == "Неправильний заголовок"