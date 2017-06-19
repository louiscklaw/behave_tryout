from behave import given, when, then, step
import os, sys

# https://github.com/appium/python-client
from appium import webdriver

from android_function import finger
from android_const import android_key_const
from android_const import android_os_permission_button

DUT_ANDROID_VERSION='7.1.1'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

@given("Agree Disclaimer Page")
def step_impl(content):
    # #### Disclaimer page
    #     * android.widget.Button -> Agree
    finger.f_ClickElementByText(content.appiumSession,'android.widget.Button' ,'Agree')

@given("Agree Privacy Policy Statements")
def step_impl(content):
    # #### Privacy Policy Statements
    #     * android.widget.Button -> Agree
    finger.f_ClickElementByText(content.appiumSession, 'android.widget.Button' ,'Agree')

# @given(u'Accept OSPermission {sPermsissionQuestions:s}')
@given(u'DENY OSPermission location')
def step_impl(content):
    # #### Allow MyObservatory to access this device's location?
    #     * android.widget.Button -> ALLOW
    # NOTE on 7.1.1 -> it is ALLOW
    # self.f_ClickElementByText('android.widget.Button' ,'ALLOW')
    # NOTE on 6.0 -> it is Allow
    # NOTE on 4.1.1 -> it doesn't appear
    finger.f_AndroidAnswerToOSPermission(content.appiumSession, android_os_permission_button.PERMISSION_DENY)


@given(u'ALLOW OSPermission location')
def step_impl(content):
    # #### Allow MyObservatory to access this device's location?
    #     * android.widget.Button -> ALLOW
    # NOTE on 7.1.1 -> it is ALLOW
    # self.f_ClickElementByText('android.widget.Button' ,'ALLOW')
    # NOTE on 6.0 -> it is Allow
    # NOTE on 4.1.1 -> it doesn't appear
    finger.f_AndroidAnswerToOSPermission(content.appiumSession, android_os_permission_button.PERMISSION_ALLOW)


@given("go through HKO App 1st launch")
def step_impl(content):
    # Accept DisclaimerPage
    f_AgreeDisclaimerPage(content.appiumSession)

@given("Close Whats New Dialog")
def step_impl(content):
    finger.f_HandleWhatsNewDialog(content.appiumSession)
    pass
