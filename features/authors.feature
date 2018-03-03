Feature: Test the authors page
  As a user
  I want to view the authors page
  So that I can see all posts

  Scenario: View all authors posts
    When The authors page loads
    Then I see all authors posts
