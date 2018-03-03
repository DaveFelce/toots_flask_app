Feature: Test a single author
  As a user
  I want to view an author page
  So that I can see their posts

  Scenario: View a single author with id 5
    When The page loads
    Then I see 3 posts from Fred