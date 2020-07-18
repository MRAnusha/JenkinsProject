*** Settings ***
Library           AppiumLibrary    run_on_failure=AppiumLibrary.CapturePageScreenshot
Library           SeleniumLibrary    run_on_failure=SeleniumLibrary.CapturePageScreenshot
Library           FakerLibrary
Library           String
Library           OperatingSystem
Library           Collections
Library           Screenshot
Library           DateTime
Library           Dialogs
Resource          ../Keywords/Web/common.robot
Resource          ../ObjectRepository/Web/buttons.robot
Resource          ../ObjectRepository/Web/images.robot
Resource          ../ObjectRepository/Web/links.robot
Resource          ../ObjectRepository/Web/textboxes.robot
Resource          ../ObjectRepository/Web/label.robot
Resource          ../ObjectRepository/Web/radiobuttons.robot
Resource          ../ObjectRepository/Web/dropdowns.robot
Resource          ../ObjectRepository/Mobile/Android/buttons.robot
Resource          ../ObjectRepository/Mobile/Android/images.robot
Resource          ../ObjectRepository/Mobile/Android/label.robot
Resource          ../ObjectRepository/Mobile/Android/links.robot
Resource          ../ObjectRepository/Mobile/Android/textboxes.robot
Resource          ../Keywords/Mobile/Android/android_common.robot
Resource          android_variables.robot
Resource          global_variables.robot
Resource          api_variables.robot
Resource          ../ObjectRepository/Web/spinner.robot
Resource          ../Keywords/Mobile/Android/android_common.robot
Resource          ../Keywords/Mobile/Android/andriod.robot
Resource          ../Keywords/API/api.robot
Resource          ../Keywords/Web/web.robot
Library           SikuliLibrary    mode=NEW
Library           ../Library/CustomLibrary.py
Library           RequestsLibrary
Library           JSONLibrary
