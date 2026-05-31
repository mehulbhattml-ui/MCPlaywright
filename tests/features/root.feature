Feature: FastMCP root page

  Scenario: Load the root page and verify the welcome message
    Given the FastMCP server is running
    When I open the root page
    Then I should see "FastMCP example server" in the page body
