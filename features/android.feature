# -- FILE: features/example.feature
Feature: Showing off behave

  Scenario: Run a simple test abotu HKO 9day forecast
    Given installed HKO App
     # go through 1st launch process
     Given Agree Disclaimer Page
     Given Agree Privacy Policy Statements

     # better handling of this
     Given ALLOW OSPermission location
     Given Close Whats New Dialog


     When we implement 5 tests
     Then behave will test them for us!

