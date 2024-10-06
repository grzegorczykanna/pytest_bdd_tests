# content of blog.feature

Feature: Blog
    Scenario: Deleting the article
        Given there is an article

        When I request the deletion of the article

        Then the request should be successful