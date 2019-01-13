# Created by davidfelce at 2019-01-13
Feature: Test a single author's data
  As a developer
  I want to test the returned data for a single author
  So that I can be sure the correct data is returned

  Scenario: View a single author with id 5
    Given A test toots file and an author id
    When I fetch the toots for a single author
    Then I get the expected data