from selenium.webdriver.common.by import By


class ForgotPasswordLocators(object):

    title_txt = (By.XPATH, "//p[text()='Forgot Password']")
    email_inp = (By.CSS_SELECTOR, "#email")
    submit_btn = (By.CSS_SELECTOR, "button[data-testid='urb-btn']")
