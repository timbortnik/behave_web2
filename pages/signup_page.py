# -*- coding: UTF-8 -*-

from .base_page import Page


class SignupPage(Page):

    """
    Signup form
    """

    url = '/account'

    def switch_to_frame(self):
        self.context.driver.switch_to.frame(self.context.driver.find_element_by_css_selector('.ds-if'))

    def get_form_field(self, field):
        # another option:
        # return self.context.driver.find_element_by_xpath('//input[contains(@placeholder, "{}")]'.format(field))
        return self.context.driver.find_element_by_xpath(
            '//label[contains(.,"{}")]/../input'.format(field))

    def get_form_field_index(self, field, idx):
        return self.context.driver.find_element_by_xpath(
            '//label[contains(.,"{}")]/../input["{}"]'.format(field, idx))

    def get_birthday_index(self, idx):
        return self.context.driver.find_element_by_xpath(
            '//span[contains(@class,"datetime-part")][{}]/input'.format(idx))

    def get_radio_field(self, field):
        return self.context.driver.find_element_by_xpath(
            '//label[text()="{}"]/preceding-sibling::input'.format(field))

    def get_submit(self):
        return self.context.driver.find_element_by_xpath(
            '//input[@type="submit" and @value="Sign-up"]')

    def fill_form_field(self, field, data):
        field = self.get_form_field(field)
        field.send_keys(data)

    def submit(self):
        self.get_submit().click()

    def get_error_text(self, text):
        return self.context.driver.find_element_by_xpath(
            '//div[@class="errortext" and text()="{}"]'.format(text))

    def fill_birthday_index(self, idx, data):
        field = self.get_birthday_index(idx)
        field.send_keys(data)
