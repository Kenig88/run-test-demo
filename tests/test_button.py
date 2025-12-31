from conftest import driver


def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element("xpath", "//input[@id='submit-id-submit']").is_displayed()
