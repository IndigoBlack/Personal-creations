from unittest.mock import patch
from wiki_summarizer import wiki_search, choose_article, summarize

#Create a test function to test the wiki_search function
@patch('requests.get')
def test_wiki_search(mock_get):
    #Initialize a variable that stores the return value of mock_get
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    mock_response.json.return_value = {
        "query": {
            "search": ["mocked data"]
        }
    }
    result = wiki_search("Python programming")
    assert result is not None
    assert isinstance(result, list)


#Create a test function to test the choose_article function
@patch('requests.get')
def test_choose_article(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "query": {
            "pages": {
                "1": {
                    "extract": "mocked data"
                }
            }
        }
    }
    result = choose_article("Python programming")
    assert result is not None
    assert isinstance(result, str)


#Create a test funtion to test the summarize function
@patch('requests.get')
def test_summarize(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "summary": "mocked data"
    }
    result = summarize("Text here")
    assert result is not None
    assert isinstance(result, str)
