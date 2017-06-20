Feature: HKO 9day forecast UI test



  Scenario Outline: Run a simple test abotu HKO 9day forecast
    Background:
      Given installed the "<App>" on "<platform>" "<type>" ver "<version>"
    Given we tap on button android.widget.TextView:text:Accessibility

    then quit appium

  Examples: Android kind
    | App       | type  | platform | version |
    | ./hko.apk | phone | Android  | 7.1.1   |
