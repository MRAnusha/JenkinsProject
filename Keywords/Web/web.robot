*** Settings ***
Resource          ../../Global/super.robot

*** Keywords ***
Create Face Book Account_1
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

Creating Face Book Account
    SeleniumLibrary.Wait Until Element Is Visible    u_0_m    ${MEDIUM_WAIT}
    SeleniumLibrary.Input Text    u_0_m    Sample
    SeleniumLibrary.Input Text    u_0_o    M
    SeleniumLibrary.Input Text    u_0_r    samplem@gmail.com
    SeleniumLibrary.Input Text    u_0_u    samplem@gmail.com
    SeleniumLibrary.Input Text    password_step_input    aabbccdd123$123
    SeleniumLibrary.Click Element    //select[@id='day']
    SeleniumLibrary.Click Element    //select[@id='day']//option[@value='14']
    SeleniumLibrary.Click Element    //select[@id='month']
    SeleniumLibrary.Click Element    //select[@id='month']/option[@value='1']
    SeleniumLibrary.Click Element    //select[@id='year']
    SeleniumLibrary.Click Element    //select[@id='year']/option[@value='1996']
    SeleniumLibrary.Scroll Element Into View    //a[text()='Create a Page']
    SeleniumLibrary.Click Element    u_0_7
    SeleniumLibrary.Wait Until Element Is Visible    u_0_12    ${MEDIUM_WAIT}
    SeleniumLibrary.Click Element    u_0_12
    SeleniumLibrary.Wait Until Element Is Visible    //button[@name='websubmit']    ${MEDIUM_WAIT}
    SeleniumLibrary.Click Element    //button[@name='websubmit']
    SeleniumLibrary.Wait Until Element Is Visible    //a[text()='Log Out']    ${MEDIUM_WAIT}
    SeleniumLibrary.Click Element    //a[text()='Log Out']
    Close All Browsers
