# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('I am on intu Signup Page')
def step_impl(context):
    context.signup_page.navigate(context.driver)
    assert context.signup_page.at()


@given('I focus on signup form')
def step_impl(context):
    context.signup_page.switch_to_frame()


@then('I see form input "{form_field}"')
def step_impl(context, form_field):
    assert context.signup_page.get_form_field(form_field) is not None


@then('I see input "{form_field}" part "{idx}"')
def step_impl(context, form_field, idx):
    assert context.signup_page.get_form_field_index(form_field, idx) is not None


@then('I see Birthday part "{idx}"')
def step_impl(context, idx):
    assert context.signup_page.get_birthday_index(idx) is not None


@then('I see radio button "{radio_field}"')
def step_impl(context, radio_field):
    assert context.signup_page.get_radio_field(radio_field) is not None


@then('I see submit button')
def step_impl(context):
    assert context.signup_page.get_submit() is not None


@given('I fill "{form_field}" with "{data}"')
def step_impl(context, form_field, data):
    context.signup_page.fill_form_field(form_field, data)


@given('I submit form')
def step_impl(context):
    context.signup_page.submit()


@then('I see error text "{error_text}"')
def step_impl(context, error_text):
    assert context.signup_page.get_error_text(error_text) is not None


@given('I am filling Birthday part "{idx}" with "{data}"')
def step_impl(context, idx, data):
    context.signup_page.fill_birthday_index(idx, data)
