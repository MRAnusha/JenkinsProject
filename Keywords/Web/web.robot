*** Settings ***
Resource          ../../Global/super.robot

*** Keywords ***
Create Face Book Account
    [Arguments]    ${facebook_data}
    SeleniumLibrary.Wait Until Element Is Visible    u_0_m    ${MEDIUM_WAIT}
    SeleniumLibrary.Input Text    u_0_m    ${facebook_data["FirstName"]}
    SeleniumLibrary.Input Text    u_0_o    ${facebook_data["SurName"]}
    SeleniumLibrary.Input Text    u_0_r    ${facebook_data["emailaddress"]}
    SeleniumLibrary.Input Text    u_0_u    ${facebook_data["emailaddress"]}
    SeleniumLibrary.Input Text    password_step_input    ${facebook_data["NewPassword"]}
    SeleniumLibrary.Click Element    //select[@id='day']
    SeleniumLibrary.Click Element    //select[@id='day']//option[@value='14']
    SeleniumLibrary.Click Element    //select[@id='month']
    SeleniumLibrary.Click Element    //select[@id='month']/option[@value='1']
    SeleniumLibrary.Click Element    //select[@id='year']
    SeleniumLibrary.Click Element    //select[@id='year']/option[@value='1996']
    SeleniumLibrary.Scroll Element Into View    //a[text()='Create a Page']
    SeleniumLibrary.Click Element    u_0_7
    Click    E:\\Jenkins\\RobotProjectJenkins\\Test-auto\\signup.png
    SeleniumLibrary.Wait Until Element Is Visible    //a[text()='Log Out']    10s
    SeleniumLibrary.Click Element    //a[text()='Log Out']
    Close All Browsers
