from behave import given, when, then, step
import os, sys

# https://github.com/appium/python-client
from appium import webdriver


DUT_DEVICE='192.168.56.102:5555'



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@given('installed "{sApkName}" on "{sPlatform}" ver "{sVersion}"')
def step_impl(content, sApkName, sPlatform ,sVersion):
    desired_caps = {}
    desired_caps['platformName'] = sPlatform
    desired_caps['platformVersion'] = sVersion
    desired_caps['deviceName'] = DUT_DEVICE

    # NOTE given that you want to install the apps
    desired_caps['app'] = PATH(sApkName)

    # output a appiumSession for latter use
    content.appiumSession = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# com.example.android.apis
@given('started {packageName} activity {sActivity} on "{sPlatform}" ver "{sVersion}"')
def step_impl(content, packageName, sActivity, sPlatform ,sVersion):
    desired_caps = {}
    desired_caps['platformName'] = sPlatform
    desired_caps['platformVersion'] = sVersion
    desired_caps['deviceName'] = DUT_DEVICE
    desired_caps['appPackage'] = packageName
    desired_caps['appActivity'] = sActivity

    # output a appiumSession for latter use
    content.appiumSession = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# debug
@then('close appium')
def step_impl(content):
    content.appium.quit()
