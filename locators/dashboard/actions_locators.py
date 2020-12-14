from selenium.webdriver.common.by import By


class ActionsLocators(object):

    title_txt = (By.XPATH, "//h2[@data-testid='default-view-header'][text()='All actions']")
    view_setting_btn = (By.XPATH, "//button[@data-testid='urb-btn']/span[text()='View Settings']")
    actions_tbl = (By.CSS_SELECTOR, "table.actions-table")
    progress_spn = (By.CSS_SELECTOR, "div[role='progressbar']")

    # Filter

    reset_view_btn = "//button[@data-testid='urb-btn']/span[text()='Reset View']"
    category_p = "//div[@data-testid='filter-summary']//p[text()='{}']"
    option_spn = "//div[@data-testid='checkbox']//span[text()='{}']"
    option_selected_str = "//div[@data-testid='checkbox']//strong[contains(text(), '{}')]"
    search_inp = (By.CSS_SELECTOR, ".expanded .input")

    # Table

    first_row = (By.CSS_SELECTOR, "tbody tr:nth-child(1)")
    rows = (By.CSS_SELECTOR, "tr.MuiTableRow-hover")
    row_number = (By.XPATH, "./td[1]")
    row_type = (By.XPATH, "./td[2]")
    row_city = (By.XPATH, "./td[10]")
