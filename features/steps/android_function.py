class finger():
    def f_ClickElementByText(appiumSession, sElement, sText):
        # AndroidAppium is expected to be a appium session
        el = appiumSession.find_element_by_android_uiautomator(
            '''new UiSelector().className("%s").text("%s")''' % (sElement, sText))
        el.click()


    # def f_AndroidAnswerToOSPermission(appiumSession, sPermission_message, Permission_Answer):
    def f_AndroidAnswerToOSPermission(appiumSession, Permission_Answer):
        # dialogAllowLocationAccess = appiumSession.find_element_by_android_uiautomator(
        #     "new UiSelector().text('%s')" % sPermission_message
        # )
        els = appiumSession.find_elements_by_android_uiautomator(
            'new UiSelector().clickable(true)'
        )
        els[Permission_Answer].click()

    def fGetDialogByTitle(appiumSession, sTitle):
        # return el that contain the sTitle
        pass

    def f_HandleWhatsNewDialog(appiumSession):
        # #### version update post
        #     * android.widget.ImageButton -> index 0
        # NOTE click the close button of the version update dialog
        try:
            appiumSession.f_ClickElementByIndex('android.widget.ImageButton' , 0)
        except Exception as e:
            pass
