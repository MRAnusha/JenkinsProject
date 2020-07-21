*** Settings ***
Resource          ../../Global/super.robot

*** Test Cases ***
TC1_Create Face Book Account
    [Setup]    Start Sikuli Process
    &{facebook}    CustomLibrary.Get Ms Excel Row Values Into Dictionary Based On Key    ${EXECDIR}\\TestData\\Testdata.xlsx    TC#11    Sheet1
    ${length}    Get Length    ${facebook}
    Run Keyword If    ${length}==0    Fail    Test data is not available, please check the test data file.
    Launch Browser and Navigate URL
    Create Face Book Account_1    ${facebook}
    [Teardown]    Stop remote server

TestCase2
    Launch Browser and Navigate URL
    Creating Face Book Account
