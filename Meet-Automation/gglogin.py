#!/usr/bin/python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def googleLogin(driver):
    driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.218024149.234410676.1609863561-284469611.1609863561&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    driver.find_element_by_id("identifierId").send_keys("YOUR_EMAIL")
    driver.find_element_by_id("identifierNext").click()
    sleep(3)
    driver.find_element_by_name("password").send_keys("YOUR_PSW")
    driver.find_element_by_id("passwordNext").click()
    sleep(3)


driver = webdriver.Firefox()


if __name__ == "__main__":

    googleLogin(driver)
