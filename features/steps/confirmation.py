# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@then('I see Confirmation Page')
def step_impl(context):
    assert context.confirmation_page.at()
