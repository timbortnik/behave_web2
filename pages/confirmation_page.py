# -*- coding: UTF-8 -*-

from .base_page import Page


class ConfirmationPage(Page):

    url = '/confirmation'

    def at(self):
        url = self.context.driver.current_url.endswith(self.url)
        text = self.context.driver.find_element_by_xpath(
            '//h1[contains(.,"Thank you for entering")]') is not None
        return url and text
