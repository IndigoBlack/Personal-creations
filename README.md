#   Title: Wiki Summarizer

    #### Description:
        I created this project as a quick way of getting the insights provided by Wikipedia articles without having to actually go to the Wikipedia website and reading their long paragraphs on a topic when I just wanted short and easily understandable overview of the topic.

        In the wiki_summarizer.py file is the main code. I created a programe that takes Whatever the user typed and searches it on wikipedia. It then first returns a list of articles numbered from 1 to whatever many articles there are, the user types in the number of the article they want to search. The articles are presented by topic so the user should be able to see which article they would like to read. To account for if the user inputs a number that isn't there the programe will ask the user again and again until the user inputs a valid number. The programe uses the wikipedia search API to be able to interact with site and get data from the site.

        Once a valid number is selected the programe will then take only the first paragraph of the aricle which because in Wikipedia the first paragraph usually gives an overview of the topic which is enough for the user to atleast get a grasp on the topic they wanted to know about. The paragraph is then parsed to a AI API to summarize it. For this topic I went with the MeaningCloud summarizer API. The AI uses extractive summarization which is basically a method that chooses sentences that based on importance to give a shorter but more understable summary of the paragraph.

        There is 3 functions in wiki_summarizer.py exluding the main function. Each function will return None if their API request was unsuccessful. After a lot of thought I decided to only use my API key at the last function for summarization as it would be annoying for the user to first have to sign up on MeaningCloud to be able to use the programe, though there is only a limited amount of time the programe can be used as I am using a MeaningCloud free tier.

        In the file test_wiki_summarizer.py is the code to test the wiki_summarizer.py code to make sure it works without needing to run the wiki_summarizer.py code everytime, which is pretty convient as the MeaningCloud API that I use can only be used a limited amount of times. I used the unittest.mock library to test the code and the API's in wiki_summarizer.py. I chose this library as I didn't want to have to rely on the API's to know if my code runs. For example, if one or both API's temporaily stop working for whatever reason my tests will still be able to run and tell me that the code runs so I wont have to change anything. I'm able to do this using the patch decorator which replaces 'requests.get' with the argument parsed in the function 'mock_get'.

        In my requiremnts.txt file is whatever I needed to pip install for the code.