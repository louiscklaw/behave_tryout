Feature: HKO 9day forecast UI test
  Scenario: Run a simple test abotu HKO 9day forecast
    Given started "com.example.android.apis" activity "com.example.android.apis.ApiDemos" on "Android" ver "7.1.1"
    when we tap on android.widget.TextView:text:Accessibility

    then close appium
