from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import re

def debug_price(url, proxy=None):
    with Stealth().use_sync(sync_playwright()) as pw:
        browser = pw.chromium.launch(
            headless=False,
            devtools=True,
            slow_mo=50,
            args=["--disable-blink-features=AutomationControlled"]
        )

        # ← Create a context that uses your proxy:
        # proxy should be a dict like:
        # { "server": "http://proxy:8000", "username": "user", "password": "pass" }
        context = browser.new_context(
            proxy=proxy,
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            ),
            locale="en-CA",
            timezone_id="America/Edmonton",
            extra_http_headers={"Accept-Language": "en-CA,en;q=0.9"},
        )

        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(3000)

        # 2) Dump visible text and scan for a price
        body_text = page.locator("body").inner_text()
        print("Body text snippet:", body_text)
        match = re.search(r"\$\s*[\d,]+(?:\.\d{2})?", body_text)
        if match:
            print("Found price:", match.group(0))
        else:
            print("No price found")

        browser.close()

if __name__ == "__main__":
    proxy_conf = proxies =  { "server": "http://207.246.206.97:8888", "username": "7zuFZFbF", "password": "4RJgcH6L"  }
    debug_price(
        "https://www.adidas.ca/en/ultraboost-1.0-shoes/HQ4202.html",
        proxy=proxy_conf
    )