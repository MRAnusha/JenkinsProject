*** Settings ***
Resource          ../../Global/super.robot

*** Keywords ***
API Response
    Create Session    ${SESSION}    ${BASE_URL}

Get Id from Public Images
    Comment    Get API Response
    ${get_All_Imag_ID}    API Response
    Comment    Create Session
    ${headers}    Create Directory    x-api-key='DEMO-API-KEY'
    Comment    Get Request from response
    ${resp1}    Get Request    ${SESSION}    /v1/images/search    headers=${headers}
    ${response_body}    Set Variable    ${resp1.json()}

Get Sub-Id from Uploaded images
    ${get_All_Imag_ID}    API Response
    ${headers}    Create Directory    x-api-key='DEMO-API-KEY'
    ${resp1}    Get Request    ${SESSION}    /v1/images    headers=${headers}
    ${response_body}    Set Variable    ${resp1.json()}

Get Name and Confidence from json response
    ${get_All_Imag_ID}    API Response
    ${headers}    Create Directory    x-api-key='DEMO-API-KEY'
    ${resp1}    Get Request    ${SESSION}    /v1/images    headers=${headers}
    ${response_body}    Set Variable    ${resp1.json()}
