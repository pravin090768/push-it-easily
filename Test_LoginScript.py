from os import utime

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import (load_dotenv, dotenv_values)
from trio import current_time

#Loading variables from .env file
load_dotenv()

options=Options()
options.add_argument("--headless")

@pytest.fixture(scope="module")
def driver():
    driver=webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.hudl.com/en_gb/")
    # accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    # accept_cookies_button.click()
    # time.sleep(2)
    # allow_all_button = driver.find_element(By.ID, "adroll_allow_all")
    # allow_all_button.click()
    # time.sleep(2)
    dropdown_button = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in')]")))
    dropdown_button.click()
    time.sleep(2)
    driver.get("https://www.hudl.com/login/")
    username = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    username.send_keys(os.getenv("USER_NAME"))
    time.sleep(2)
    continue_button = driver.find_element(By.NAME, "action")
    continue_button.click()
    time.sleep(2)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys(os.getenv("USER_PASSWORD"))
    time.sleep(2)
    continue_button = driver.find_element(By.NAME, "action")
    continue_button.click()
    time.sleep(2)
    actual_title = driver.title
    expected_title = "Home - Hudl"
    if expected_title not in actual_title:
        raise AssertionError("Login failed")
    # dismiss_button=driver.find_element(By.CSS_SELECTOR, "[class='u-onboarding-custom__dismiss']")
    # dismiss_button.click()
    # time.sleep(6)
    profile_button=driver.find_element(By.CSS_SELECTOR, "[class='hui-globaluseritem__display-name']")
    profile_button.click()
    time.sleep(3)
    logout_button=driver.find_element(By.XPATH, "//span[text()='Log Out']")
    logout_button.click()
    time.sleep(3)

def test_invalid_login(driver):
    driver.get("https://www.hudl.com/en_gb/")
    dropdown_button = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in')]")))
    dropdown_button.click()
    time.sleep(2)
    driver.get("https://www.hudl.com/login/")
    time.sleep(2)
    username = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    username.send_keys("amita_shetty@yahoo.com")
    time.sleep(2)
    continue_button = driver.find_element(By.NAME, "action")
    continue_button.click()
    time.sleep(2)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("wrongpassword")
    time.sleep(2)
    continue_button = driver.find_element(By.NAME, "action")
    continue_button.click()
    time.sleep(2)
    actual_error_box=driver.find_element(By.ID,"error-element-password")
    assert "Your email or password is incorrect. Try again." in actual_error_box.text, "Displayed error is not as expected"

def test_invalid_login_blank_username(driver):
    driver.get("https://www.hudl.com/en_gb/")
    time.sleep(2)
    dropdown_button = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in')]")))
    dropdown_button.click()
    time.sleep(2)
    driver.get("https://www.hudl.com/login/")
    time.sleep(2)
    username = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    username.send_keys("abc")
    time.sleep(2)
    continue_button = driver.find_element(By.NAME, "action")
    continue_button.click()
    time.sleep(2)
    actual_error_box=driver.find_element(By.ID,"error-element-username")
    assert "Enter a valid email." in actual_error_box.text, "Displayed error is not as expected"


