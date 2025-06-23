class CookieModal:
    def __init__(self, page):
        self.page = page

    def wait_for_modal(self):
        try:
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_selector(".cookie-policy-content", timeout=5000)
        except Exception:
            print("Missing cookies modal!")

    def accept_analytics(self):
        self.page.get_by_role("button", name="Dostosuj").click()
        self.page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
        self.page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    