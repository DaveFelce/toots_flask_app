from behave import *
from nose.tools import *


@when(u'The authors page loads')
def step_impl(context):

    context.browser.get('http://127.0.0.1:5000/authors')


@then(u'I see all authors posts')
def step_impl(context):

    browser = context.browser

    assert_in('<span><a href="/author/3">Dennis</a></span>', browser.page_source)
    assert_in('<span>doot noot!</span>', browser.page_source)
    assert_in('<span>zoot choot!</span>', browser.page_source)
    assert_equal('Toots!', browser.title)

    charlie_links = browser.find_elements_by_link_text('Charlie')
    assert_equal(len(charlie_links), 13)
