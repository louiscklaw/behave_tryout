from behave import given, when, then, step
import os
import sys

# https://github.com/appium/python-client
from appium import webdriver
import android_capabilities


DUT_DEVICE = '192.168.56.102:5555'


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# @given('installed "{sApkName}" on "{sPlatform}" ver "{sVersion}"')
@given('installed the "{App}" on "{platform}" "{type}" ver "{version}"')
def install_android_application(content, App, type, platform, version):
    # desired_caps = {}
    # desired_caps['platformName'] = sPlatform
    # desired_caps['platformVersion'] = sVersion
    # desired_caps['deviceName'] = DUT_DEVICE

    # # NOTE given that you want to install the apps
    # desired_caps['app'] = PATH(sApkName)

    # # output a appiumSession for latter use
    # content.appiumSession = webdriver.Remote(
    #     'http://localhost:4723/wd/hub', desired_caps)
    # NOTE expecting iOS/Android
    sPlatformName = platform

    wd = ''

    desired_caps = {}
    desired_caps['platformName'] = sPlatformName
    desired_caps['platformVersion'] = version
    desired_caps['deviceName'] = DUT_DEVICE

    desired_caps['newCommandTimeout'] = 240
    # output a appiumSession for latter use

    # NOTE given that you want to install the apps
    if sPlatformName.upper() in ['ANDROID']:
        desired_caps['app'] = PATH(App)
    else:
        # TODO cater android only
        pass

    wd = webdriver.Remote(
        'http://localhost:4723/wd/hub', desired_caps)

    content.appiumSession = wd

    pass


# com.example.android.apis
@given('started {packageName} activity {sActivity} on "{sPlatform}" ver "{sVersion}"')
def step_impl(content, packageName, sActivity, sPlatform, sVersion):
    desired_caps = {}
    desired_caps['platformName'] = sPlatform
    desired_caps['platformVersion'] = sVersion
    desired_caps['deviceName'] = DUT_DEVICE
    desired_caps['appPackage'] = packageName
    desired_caps['appActivity'] = sActivity

    # output a appiumSession for latter use
    content.appiumSession = webdriver.Remote(
        'http://localhost:4723/wd/hub', desired_caps)

# debug


@then('quit appium')
def quit_appium(content):
    if hasattr(content, 'appiumSession'):
        # content.appiumSession.quit()
        pass
