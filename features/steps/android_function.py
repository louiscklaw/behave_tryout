from time import sleep
import logging


class finger():
    def f_ClickElementByText(appiumSession, sElement, sText):
        # AndroidAppium is expected to be a appium session
        el = appiumSession.find_element_by_android_uiautomator(
            '''new UiSelector().className("%s").text("%s")''' % (sElement, sText))
        el.click()


    def f_ClickElementByIndex(appiumSession, sElement, iIdx):
        el = appiumSession.find_elements_by_android_uiautomator(
            '''new UiSelector().className("%s")''' % sElement)[iIdx]
        el.click()


    # def f_AndroidAnswerToOSPermission(appiumSession, sPermission_message, Permission_Answer):
    def f_AndroidAnswerToOSPermission(appiumSession, sPermission_message, Permission_Answer):
        if appiumSession.find_element_by_android_uiautomator(
            '''new UiSelector().text("Allow MyObservatory to access this device's location?")'''
        ):
            els = appiumSession.find_elements_by_android_uiautomator(
                'new UiSelector().clickable(true)'
            )
            els[Permission_Answer].click()
        else:
            # TODO handling here
            pass

    def f_FindTargetByXPath(appiumSession, sWidget, sProperties, sValue):
        return appiumSession.find_elements_by_xpath(
            '//%s[@%s="%s"]' % (sWidget, sProperties, sValue)
            )


    def f_TapWidgetByPropertiesAndValue(appiumSession, sWidget, sProperties, sValue):
        # NOTE try to reach the clickable thing buy it properties,
        # otherwise, find it's parents
        els=f_FindTargetByXPath(appiumSession, sWidget, sProperties, sValue)
        if els:
            sleep(1)
            els[0].click()
            raise('thing found')
        pass

    def f_click_natvigate_button(appiumSession):
        if DUT_ANDROID_VERSION in ['4.1.1']:
            # NOTE for android 4.1.1 , this works
            appiumSession.f_ClickElementByDesc('android.widget.ImageButton' ,'Navigate')
        else:
            # NOTE sorry for dirtyhack, but with the given time i cannot find the efficient addressing method for this button
            # position of button [0,96][224,320]
            diNatvigateButtonCenter = (int(224/2),int((320-96)/2))
            appiumSession.driver.tap([diNatvigateButtonCenter], 1)


    def fGetDialogByTitle(appiumSession, sTitle):
        # return el that contain the sTitle
        pass

    def f_HandleWhatsNewDialog(appiumSession):
        # #### version update post
        #     * android.widget.ImageButton -> index 0
        # NOTE click the close button of the version update dialog

        # TODO better handling of this
        iCountDown = 5
        bContinueWait=True

        sleep(10)
        finger.f_ClickElementByIndex(appiumSession, 'android.widget.ImageButton' , 0)


        # try:
        #     while iCountDown:
        #         if appiumSession.find_elements_by_android_uiautomator(
        #             'new UiSelector().textStartsWith("What\'s New in Version")'
        #         ):
        #             bContinueWait=False
        #         else:
        #             iCountDown-=1
        #             sleep(1)

        #         if iCountDown ==0:
        #             # TODO how to handle the interruption ?
        #             raise('cannot close dialog')


        # except Exception as e:

        #     pass

    def f_PressKey(appiumSession, sKey):
        appiumSession.press_keycode(sKey)
