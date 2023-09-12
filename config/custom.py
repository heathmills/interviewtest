from selenium.webdriver.common.by import By

def find_element_by_data_qa_id(data_value):
    locator = (By.CSS_SELECTOR, f"[data-qa-id='{data_value}']")
    return locator