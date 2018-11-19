import pytest

from ..search import Search

def test_builtLink():
    tmpSearch = Search()
    tmpSearch.setEngine("duckduckgo")
    tmpSearch.setDomain("com")
    tmpSearch.setQuery(["test", "query"])
    assert tmpSearch.buildLink() == "https://duckduckgo.com/?q=test+query"
    