#!/usr/bin/env python

from selenium.webdriver import PhantomJS
from getpass import getpass
import requests, sys, time

if sys.version_info.major == 2:
    input = raw_input

if __name__ == "__main__":
    
    driver = PhantomJS()

    gh_user = input("Please enter GitHub username: ")

    gh_pass = getpass("Password for {0}@github.com: ".format(gh_user))

    python_crawler_html = requests.get("https://raw.githubusercontent.com/c3h3/PyCon2015-Crawlers/master/Course_Info/python-crawler.html", auth=(gh_user, gh_pass)).text

    if python_crawler_html == "Not Found":
        raise ValueError("Username or Password is incorrect.")

    kktix_user = input("Please enter KKTIX username: ")

    kktix_pass = getpass("Password for {0}: ".format(kktix_user))

    driver.get("https://kktix.com/users/sign_in?back_to=https://kktix.com/dashboard/events/python-crawler/edit")

    driver.find_element_by_id("user_login").send_keys(kktix_user)
    driver.find_element_by_id("user_password").send_keys(kktix_pass)
    driver.find_element_by_name("commit").click()

    if driver.current_url == "https://kktix.com/users/sign_in":
        raise ValueError("Username or Password is incorrect.")

    time.sleep(0.5)

    driver.find_element_by_class_name("cke_button__source").click()

    driver.find_element_by_class_name("cke_source").clear()

    driver.find_element_by_class_name("cke_source").send_keys(python_crawler_html)

    driver.find_element_by_css_selector(".form-actions .btn.btn-primary").click()

    print("Done")
