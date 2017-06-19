#!/usr/bin/zsh

kill $(ps -aux |grep -i appium|grep -i node|awk '{print $2}')
appium &
sleep 5
behave


