from behave import given, when, then, step
import os, sys

# https://github.com/appium/python-client
from appium import webdriver

DUT_ANDROID_VERSION='7.1.1'

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@given("installed HKO App")
def step_impl(content):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = DUT_ANDROID_VERSION
    desired_caps['deviceName'] = '192.168.56.102:5555'


    # NOTE given that you want to install the apps
    desired_caps['app'] = PATH(
        #'../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
        # './sample-code/sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
        './hko.apk'
    )

    # output a appiumSession for latter use
    content.appiumSession = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
