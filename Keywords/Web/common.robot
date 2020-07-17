*** Settings ***
Resource          ../../Global/super.robot

*** Keywords ***
Launch Browser and Navigate URL
    SeleniumLibrary.Open Browser    ${FACEBOKK_URL}    ${BROWSER_NAME}
    SeleniumLibrary.Maximize Browser Window
