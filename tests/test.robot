
*** Settings ***
Variables   ../resources/config.py

Library    PageObjectLibrary
Library    SeleniumLibrary
Library    Process

Suite Setup       Start browser
Suite Teardown    Close browsers



*** Variables ***
${BROWSER}    chrome

*** Keywords ***
Start browser
    open browser    ${CONFIG.base_url}    ${BROWSER}

Close browsers
    Close all browsers


*** Test Cases ***

Verify that a modal with the text "Thanks for submitting the form" is shown when a user completes the form
    [Setup]    Go to page    LoginPage
    Fill form
    The modal should have the text    Thanks for submitting the form

Verify that a modal with the text "Small Modal" is shown when the user clicks the Small modal button
    [Setup]    Go to Page    ModalPage
    Click small modal button
    Verify the text    Small Modal






