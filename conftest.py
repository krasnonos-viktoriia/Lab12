import os
import pytest
import pytest_asyncio
import allure
from playwright.async_api import async_playwright


@pytest_asyncio.fixture
async def page(request):
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("traces", exist_ok=True)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()

        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = await context.new_page()

        yield page

        test_name = request.node.name
        trace_path = f"traces/{test_name}.zip"

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot = await page.screenshot(
                path=f"screenshots/{test_name}_failure.png"
            )

            allure.attach(
                screenshot,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        await context.tracing.stop(path=trace_path)

        if os.path.exists(trace_path):
            allure.attach.file(
                trace_path,
                name=f"{test_name}_trace",
                attachment_type=allure.attachment_type.ZIP
            )

        await browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)