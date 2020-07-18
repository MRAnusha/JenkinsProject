*** Settings ***
Resource          ../../Global/super.robot

*** Test Cases ***
TC_01_Validate Id from All Public Images
    Get Id from Public Images

TC_02_Validate Sub-ID from Uploaded Images
    Get Sub-Id from Uploaded images

TC_03_Validate Name and Confidence from JSON Response
    Get Name and Confidence from json response
