*** Settings ***
Resource          ../../Global/super.robot

*** Test Cases ***
TC1_Create Face Book Account
    [Setup]    Start Sikuli Process
    &{facebook}    CustomLibrary.Get Ms Excel Row Values Into Dictionary Based On Key    ${EXECDIR}\\TestData\\Testdata.xlsx    TC#11    Sheet1
    ${length}    Get Length    ${facebook}
    Run Keyword If    ${length}==0    Fail    Test data is not available, please check the test data file.
    Launch Browser and Navigate URL
    Create Face Book Account    ${facebook}
    [Teardown]    Stop remote server

TestCase2
    Launch Browser and Navigate URL
    Comment    SeleniumLibrary.Click Element    u_0_2
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
