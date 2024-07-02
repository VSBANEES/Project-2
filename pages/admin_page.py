from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_page_title = (By.XPATH, "//h1[text()='Admin']")
        self.menu_items = {
            "User Management": (By.ID, "menu_admin_UserManagement"),
            "Job": (By.ID, "menu_admin_Job"),
            "Organization": (By.ID, "menu_admin_Organization"),
            "Qualifications": (By.ID, "menu_admin_qualifications"),
            "Nationalities": (By.ID, "menu_admin_nationality"),
            "Corporate Banking": (By.ID, "menu_admin_banking"),
            "Configuration": (By.ID, "menu_admin_Configuration"),
            # Add more menu items as needed
        }

    def get_admin_page_title(self):
        return self.driver.find_element(*self.admin_page_title).text

    def is_menu_item_displayed(self, item_name):
        return self.driver.find_element(*self.menu_items[item_name]).is_displayed()
