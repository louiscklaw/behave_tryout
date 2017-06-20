from behave import given, when, then, step
import os
import sys

# https://github.com/appium/python-client
from appium import webdriver

from android_function import finger
from android_const import android_key_const
from android_const import android_os_permission_button

from time import sleep


@given("Agree Disclaimer Page")
def step_impl(content):
    # #### Disclaimer page
    #     * android.widget.Button -> Agree
    finger.f_ClickElementByText(
        content.appiumSession,
        'android.widget.Button', 'Agree')


@given("Agree Privacy Policy Statements")
def step_impl(content):
    # #### Privacy Policy Statements
    #     * android.widget.Button -> Agree
    finger.f_ClickElementByText(
        content.appiumSession,
        'android.widget.Button', 'Agree')

# @given(u'Accept OSPermission {sPermsissionQuestions:s}')


@given(u'DENY OSPermission location')
def step_impl(content):
    # #### Allow MyObservatory to access this device's location?
    #     * android.widget.Button -> ALLOW
    # NOTE on 7.1.1 -> it is ALLOW
    # self.f_ClickElementByText('android.widget.Button' ,'ALLOW')
    # NOTE on 6.0 -> it is Allow
    # NOTE on 4.1.1 -> it doesn't appear
    finger.f_AndroidAnswerToOSPermission(
        content.appiumSession,
        android_os_permission_button.PERMISSION_DENY)


@given(u'{sAnswer} OSPermission {sQuestion}')
def step_impl(content, sQuestion, sAnswer):
    # #### Allow MyObservatory to access this device's location?
    #     * android.widget.Button -> ALLOW
    # NOTE on 7.1.1 -> it is ALLOW
    # self.f_ClickElementByText('android.widget.Button' ,'ALLOW')
    # NOTE on 6.0 -> it is Allow
    # NOTE on 4.1.1 -> it doesn't appear
    if sAnswer.upper() == 'ALLOW':
        finger.f_AndroidAnswerToOSPermission(
            content.appiumSession,
            sQuestion, android_os_permission_button.PERMISSION_ALLOW)
    elif sAnswer.upper() == 'DENY':
        finger.f_AndroidAnswerToOSPermission(
            content.appiumSession,
            sQuestion, android_os_permission_button.PERMISSION_DENY)
    else:
        # logging.error('unhandled option %s' % sAnswer)
        pass


@given("go through HKO App 1st launch")
def step_impl(content):
    # Accept DisclaimerPage
    f_AgreeDisclaimerPage(content.appiumSession)
    pass


@given('Close "{sText}"')
def step_impl(content, sText):
    finger.f_HandleWhatsNewDialog(content.appiumSession)
    pass


@given('tap on button "{sWidget}":"{sProperties}":"{sDescription}"')
def step_impl(content, sWidget, sProperties, sDescription):
    finger.f_TapWidgetByPropertiesAndValue(
        content.appiumSession,
        sWidget, sProperties, sDescription)
    sleep(1)
    pass


@given('tap on specific location "{iX:d}":"{iY:d}"')
def step_impl(content, iX, iY):
    content.appiumSession.tap([(iX, iY)], 1)
    sleep(1)
    pass


@given('press "{dPadKey}" until "{sWidget}":"{sProp}":"{sTarget}" appears')
def step_impl(content, sWidget, sProp, sTarget, dPadKey):
    iCountDown = 15
    bFound = False

    # NOTE text to key constant
    if dPadKey.upper() == 'DOWN':
        dPadKey = android_key_const.KEYCODE_DPAD_DOWN

    while not(bFound) or bRetry:
        els = finger.f_FindTargetByXPath(
            content.appiumSession,
            sWidget, sProp, sTarget)
        if els:
            bFound = True
            bRetry = False
        else:
            iCountDown -= 1
            finger.f_PressKey(content.appiumSession,
                              dPadKey)

        if iCountDown == 0:
            bRetry = False

    if not(bFound):
        raise('wanted %s not found')


# try space with space
@given("try {sSpace}")
def step_impl(content, sSpace):
    print(sSpace)


def after_scenario(content):
    # NOTE quit appoim session created
    if content.appiumSession:
        content.appiumSession.quit()
