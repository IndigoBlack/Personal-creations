import requests

"""A programe that searches for an article on wikipedia for the topic the user typed in and then
    summarizes the overview of the article using an AI API then prints the link to the full article at the end."""


def main():
    #Get the user-input topic
    topic = input("Enter search: ")
    #Parse the user input into the wiki_search function
    result = wiki_search(topic)
    #Check if the wiki_search function returned something
    if result:
        print(f"Searching for {topic}")
        #Print the result of the search in a numbered format starting from 1
        for j, i in enumerate(result, start=1):
            print(j, i["title"])
        #Ask the user for the article they want
        choice = int(input("choose article number: "))
        #Check if the user selected an article that is within range
        try:
            #Initiate the chosen article into a variable
            article_chosen = result[choice -1]["title"]
        except IndexError:
            while choice not in range(1, len(result) + 1):
                print(f"Please choose a number between 1 and {len(result)}")
                choice = int(input("choose article number: "))
            article_chosen = result[choice -1]["title"]
        #Parse the chosen article to the function choose_article
        article = choose_article(article_chosen)
        #Print the summarized result using the summarize function
        summarized_article = summarize(article)
        print(summarized_article)
        #Print the link to the full article
        article_chosen = article_chosen.replace(" ", "_")
        print(f"\nLink: https://en.wikipedia.org/wiki/{article_chosen}")

#Parse the user-input into the wikisearch API
def wiki_search(s):
    link = "https://en.wikipedia.org/w/api.php"
    #Specify the parameter for the API request
    parameters = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": s,
    }
    #Make a API request to wikipedia API
    wiki = requests.get(link, params=parameters)
    #Check if the request was successful
    if wiki.status_code == 200:
        #Put the result of the request into a json format response
        data = wiki.json()
        #Initiate a variable named search the search result of the user's topic
        search = data["query"]["search"]
        #Return the the search results
        if search == []:
            print("Topic not found")
        return search
    else:
        #If the request was unsuccessful return something to indicate this
        print("Unable to get search results")
        return None


#Get the article
def choose_article(s):
    link = "https://en.wikipedia.org/w/api.php"
    #Specify the parameters for the API request
    parameters = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": s,
        "explaintext": True,
        "exintro": True,
        "exlimit": 1,
    }
    #Make the wikipedia API request
    wiki = requests.get(link, params=parameters)
    #check if the request was successful
    if wiki.status_code == 200:
        #If the request was successful turn the result into json format
        data = wiki.json()
        article_nr = list(data["query"]["pages"].keys())[0]
        #print(article_nr)
        #Parse the article into a variable
        content = data["query"]["pages"][article_nr]["extract"]
        #print(content)
        return content
    else:
        return None


#Use the AI API to summarize the article
def summarize(s):
    #Initiate the API key to a variable
    API_key = "API Key"
    #Specify the parameters for the AI(Meaning Cloud) API
    parameters = {
        "key": API_key,
        "txt": s,
        "sentences": 50
    }
    summarise = "https://api.meaningcloud.com/summarization-1.0"
    #Use try and except to catch any exceptions
    try:
        #Make the API request to summarize the article
        response = requests.get(summarise, params=parameters)
        #print(response.text)
        #check if the the request was successful
        if response.status_code == 200:
            #If the request was successful turn it into a json format
            response_edit = response.json()
           #print(response_edit)
            #Put the summarized article into a variable
            result = response_edit["summary"]
            #Return the summarized article
            return f"Summary \n\n{result}"
        else:
            #If the response was unsuccessful print somthing to show it wasn't then return none
            print("Status code is not 200")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured while summarizing the article: {e}")
        return None


if __name__ == "__main__":
    main()


