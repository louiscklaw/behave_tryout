# -- FILE: features/example.feature
# https://jenisys.github.io/behave.example/intro.html

Feature: HKO 9day forecast UI test
  Scenario Outline: Run a simple test abotu HKO 9day forecast
    Given installed the "<App>" on "<platform>" "<type>" ver "<version>"
     # go through 1st launch process
     and Agree Disclaimer Page
     and Agree Privacy Policy Statements

     # better handling of this
     and ALLOW OSPermission "Allow MyObservatory to access this device's location?"
     and Close "What's New Dialog"

     # doen 1st launch greetings
     #When we tap on "android.widget.ImageButton":"content-desc":"Navigate up"
     #When we tap on "android.widget.TextView":"text":"MyObservatory"

     # Natvigate to 9 day forecast page
     Given tap on specific location "112":"112"
     and press "DOWN" (max: 15) and "android.widget.TextView":"text":HK 9-Day Forecast appears
     and tap on button "android.widget.TextView":"text":"HK 9-Day Forecast"

     # Expect
     Then Fail if the "HK 9-Day Forecast" not appears on screen

     # Expect
     Then press "DOWN" (max: 15) and "android.widget.TextView":"text":9day weather forecast appears


  Examples: Android kind
    | App       | type  | platform | version |
    | ./hko.apk | phone | Android  | 7.1.1   |

