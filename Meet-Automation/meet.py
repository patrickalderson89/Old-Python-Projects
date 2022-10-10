#!/usr/bin/python3

import gglogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = gglogin.driver
gglogin.googleLogin(driver)
meet_url = driver.current_url
while True:
    driver.find_element_by_class_name("cmvVG").click()
    sleep(3)
    driver.find_element_by_class_name("poFWNe.zHQkBf").send_keys("CLASS_CODE")
    sleep(1)
    driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
    if meet_url == driver.current_url:      # if class has not started yet, try again
        sleep(120)

