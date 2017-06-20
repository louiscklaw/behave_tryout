# -- FILE: features/example.feature
# https://jenisys.github.io/behave.example/intro.html

Feature: HKO 9day forecast UI test
  Background:
     | platform  | version     |
     | Android   | 7.1.1       |
    Given installed "./hko.apk" on <mobile> ver <version>
     # go through 1st launch process
     and Agree Disclaimer Page
     and Agree Privacy Policy Statements

     # better handling of this
     and ALLOW OSPermission "Allow MyObservatory to access this device's location?"
     and Close "What's New Dialog"

  Scenario: Run a simple test abotu HKO 9day forecast
     #When we tap on "android.widget.ImageButton":"content-desc":"Navigate up"
     #When we tap on "android.widget.TextView":"text":"MyObservatory"
     Given we tap on specific location "112":"112"
     and press "DOWN" until "android.widget.TextView":"text":"HK 9-Day Forecast" appears
     #and tap on "HK 9-Day Forecast"

     #then 9days forecast view comes up
     #and with the description
     #and with the 1st day forecast
     #and with the 2st day forecast
     #and with the 3st day forecast

     #then scroll down
     #and with the 4st day forecast
     #and with the 5st day forecast
     #and with the 6st day forecast

     #then scroll down
     #and with the 7st day forecast
     #and with the 8st day forecast
     #and with the 9st day forecast




