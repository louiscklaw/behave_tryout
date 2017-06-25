# python android app tester (HKO)

### environment: 
    * linux
    * appium
    * python 3.6.1, behave, python-appium-client
        * to setup
    ```
pip install -r requirements.txt
    ```


### to execute:
    * setup virtual environment
    ```shell
source venv/bin/activate
    ```
    * start appium -> connect to android / genymotion
    ```
appium
    ```
    * python behave
    ```shell
behave ./features/HKOApp_9DayForecast.feature 
    ```



