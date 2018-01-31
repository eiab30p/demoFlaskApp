"""
Testing For Email.

This is simple a basic Email Test.
"""
import unittest
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def input_set_text(driver, element_id, text):
    """
    Fill input with id of element_id with text.

    returns input element
    """
    el = driver.find_element_by_id(element_id)
    el.clear()
    el.send_keys(text)

    return el


class TestEmail(unittest.TestCase):
    """
    Test Email Function Class.

    This Class uses Selenium to test the UI to send an email. It includes
    the set up, test, and tear down.
    """

    def setUp(self):
        """
        Set Up Connection.

        setUp ensures you are using a WebDriver, goes to the website, and then
        set the size of the screen.
        """
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('D:/chromedriver.exe')
        # self.driver = webdriver.Ie()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("http://192.168.50.11:5000/")
        # driver.get("ServerIP")
        # driver.set_window_size("1024", "768")
        driver.maximize_window()

    def tearDown(self):
        """
        Tear Down.

        This simply closes all the windows.
        """
        self.driver.close()

    def test_email_other(self):
        """
        Test Email Function.

        This will Go to the Website, ensures the site is WTE.
        Once it knows it is at the right site it will go to the
        contact tab and then send an email to an email address.
        """
        driver = self.driver

        # Check Main Title
        self.assertIn("What The Eddy", driver.title)
        elem = driver.find_element_by_css_selector(".title")
        self.assertIn("Welcome! Stranger", elem.text)

        contact_navLink = driver.find_element_by_link_text("contact")
        contact_navLink.click()

        self.assertIn("Contact - WTE", driver.title)
        time.sleep(2)

        input_set_text(driver, "first_name", "Eddy")
        input_set_text(driver, "middle_name", "Ewjkhka")
        input_set_text(driver, "last_name", "Eddy")
        input_set_text(driver, "email", "")
        driver.find_element_by_id("accept_tos").click()
        input_set_text(driver, "email_message", "Some Other Stuff")
        submit = driver.find_element_by_css_selector("#submit").click()
        time.sleep(5)

        # Assert error message is shown
        error_message = self.driver.find_element_by_class_name(
            "email_error").text

        assert "Please Enter Your Email" in error_message

        return submit

    def test_email(self):
        """
        Test Email Function.

        This will Go to the Website, ensures the site is WTE.
        Once it knows it is at the right site it will go to the
        contact tab and then send an email to an email address.
        """
        driver = self.driver

        # Check Main Title
        self.assertIn("What The Eddy", driver.title)
        elem = driver.find_element_by_css_selector(".title")
        self.assertIn("Welcome! Stranger", elem.text)

        contact_navLink = driver.find_element_by_link_text("contact")
        contact_navLink.click()

        self.assertIn("Contact - WTE", driver.title)
        input_set_text(driver, "first_name", "Eddy")
        input_set_text(driver, "middle_name", "E")
        input_set_text(driver, "last_name", "Eddy")
        input_set_text(driver, "email", "Eduardo.Eddy.Verde94@gmail.com")
        # checkbox
        driver.find_element_by_id("accept_tos").click()
        input_set_text(driver, "email_message", "Some Other Stuff")
        submit = driver.find_element_by_css_selector("#submit").click()
        return submit


if __name__ == '__main__':
    unittest.main()
