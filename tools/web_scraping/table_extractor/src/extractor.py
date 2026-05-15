import requests

def fetch_html(url):
    # Send GET request to fetch url data
    response = requests.get(url)
    
    #if status code is not 200 (OK)
    if response.status_code != 200:
        #Raise Exception
        raise Exception(f"Failed request: {response.status_code}")

    #else returns the text contents
    return response.text