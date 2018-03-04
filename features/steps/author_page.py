from behave import *
from nose.tools import *


@when(u'The page loads')
def step_load_page(context):

    context.browser.get('http://127.0.0.1:5000/author/2')


@then(u'I see 3 posts from Fred')
def step_should_be_three_fred_posts(context):

    browser = context.browser

    assert_not_in('<span><a href="/author/3">Dennis</a></span>', browser.page_source)
    assert_not_in('<span>doot noot!</span>', browser.page_source)
    assert_in('<span>zoot choot!</span>', browser.page_source)
    assert_equal('Toots by author', browser.title)

    charlie_links = browser.find_elements_by_link_text('Charlie')
    assert_equal(len(charlie_links), 10)
