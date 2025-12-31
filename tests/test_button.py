from conftest import driver


def test_button_1_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element("xpath", "//input[@id='submit-id-submit']").is_displayed()


def test_button_2_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button")
    assert driver.find_element("xpath", "//a[text()='Click']").is_displayed()