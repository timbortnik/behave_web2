# -*- coding: UTF-8 -*-
"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

"""

from selenium import webdriver
from pages.signup_page import SignupPage
from pages.confirmation_page import ConfirmationPage
import selenium.webdriver.support.ui as ui
import datetime
import time


def get_date_time():
    dt_format = '%Y%m%d_%H%M%S'
    return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)


def before_all(context):                        # TODO add 2nd driver
    context.base_url = "https://intu.co.uk"
    context.driver = webdriver.Chrome()
    context.wait = ui.WebDriverWait(context.driver, 10)
    context.signup_page = SignupPage(context)
    context.confirmation_page = ConfirmationPage(context)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot('scenario_result/' + scenario.name + get_date_time() + "_failed.png")
        file = open('scenario_result/' + scenario.name + get_date_time() + '.html', 'w')
        file.write(context.driver.page_source)
        file.close()

def after_all(context):
    context.driver.quit()
