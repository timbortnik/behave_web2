Feature: Showing off behave and selenium for intu Signup

@wip
Scenario: Sign up form elements
    Given I am on intu Signup page
    And I focus on signup form
    Then I see form input "First name"
    And I see form input "Last name"
    And I see form input "Email address"
    And I see Birthday part "1"
    And I see Birthday part "2"
    And I see Birthday part "3"
    And I see radio button "Female"
    And I see radio button "Male"
    And I see radio button "Prefer not to say"
    And I see form input "Postcode"
    And I see submit button

Scenario: Sign up form check e-mail required
    Given I am on intu Signup page
    And I focus on signup form
    And I fill "First name" with "John"
    And I fill "Last name" with "Doe"
    And I submit form
    Then I see error text "Please enter your email address"
    And I see error text "Please enter your birthday"

Scenario: Sign up form submitted
    Given I am on intu Signup page
    And I focus on signup form
    And I fill "First name" with "John"
    And I fill "Last name" with "Doe"
    And I fill "Email address" with "JDoe@restmail.net"
    And I am filling Birthday part "1" with "11"
    And I am filling Birthday part "2" with "01"
    And I am filling Birthday part "3" with "1911"
    And I submit form
    Then I see Confirmation Page
    # TODO: check if the e-mail arrived @restmail
