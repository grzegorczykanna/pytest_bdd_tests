# content of test_blog.py

from pytest_bdd import scenarios, given, when, then

from my_app.models import Article

scenarios("blog.feature")


@given("there is an article", target_fixture="article")
def there_is_an_article():
    return Article()


@when("I request the deletion of the article", target_fixture="request_result")
def there_should_be_a_new_article(article, http_client):
    return http_client.delete(f"/articles/{article.uid}")


@then("the request should be successful")
def article_is_published(request_result):
    assert request_result.status_code == 200