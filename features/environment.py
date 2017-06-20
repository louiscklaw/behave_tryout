# -- FILE:features/environment.py
from appium import webdriver

DUT_DEVICE = '192.168.56.102:5555'

sApkName = './hko.apk'

# def before_all(content):
#     content.config.setup_logging()


# def after_scenario(content):
#     content.appiumSession.quit()

def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


sHKOAppId = 'hko.MyObservatory_v1_0'


def uninstall_app(content, app_id):
    content.appiumSession.remove_app(app_id)
    pass


def quit_appiumSession(content):
    content.appiumSession.quit()
    pass


def before_feature(content, feature):
    pass


def before_scensrio(content, scenario):
    pass


def after_scenario(content, scenario):
    if hasattr(content, 'appiumSession'):
        uninstall_app(content, sHKOAppId)
        quit_appiumSession(content)
        print('uninstall application')
    pass
