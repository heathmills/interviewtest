Feature: Login page

    Background:
        Given User is on login page

    Scenario: Login success as registered user
        When User enters valid email address
        And User enters valid password
        And Clicks Login
        Then User is logged in successfully

    Scenario: Login unsuccessful with invalid email address
        When User enters invalid email address
        And Clicks Login
        Then Login error message is displayed

    Scenario: Login unsuccessful with unregistered email address
        When User enters unregistered email address
        And Clicks Login
        Then Login error message is displayed

    Scenario: Error displayed for empty password fields
        When User enters valid email address
        And Clicks Login
        Then Login error message is displayed

    Scenario: Error displayed for empty login form
        When Clicks Login
        Then Login error message is displayed

    Scenario: User's email is prefilled when remember me is selected
        When User fills in valid credentials
        And Selects remember me
        And Clicks Login
        And User is logged in successfully
        When User logs out of account
        And User navigates to login page
        Then Email address should be auto filled in

    Scenario: Error is displayed when unregistered user logs in with organisation
        When User clicks login with an organisation
        And User enters their email address
        And Clicks login on organisation page
        Then Error message is displayed for organisation login