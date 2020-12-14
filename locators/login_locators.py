from selenium.webdriver.common.by import By


class LoginLocators(object):

    title_txt = (By.XPATH, "//p[text()='Sign In']")
    error_msg = (By.CSS_SELECTOR, "div[class^='Alert__AlertTypography']")

    # Login

    user_inp = (By.CSS_SELECTOR, "#email")
    pass_inp = (By.CSS_SELECTOR, "#password")
    submit_btn = (By.CSS_SELECTOR, "button[data-testid='urb-btn']")

    # Forgot password

    forgot_pass_lnk = (By.XPATH, "//p[text()='Forgot Password']")
