# Uncomment the imports below before you add the function code
import requests
# I uncommented the import requests bfore I added the function code.
import os
from dotenv import load_dotenv
import json
from django.http import JsonResponse

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# In the previous lab, I have created API endpoints to fetchReviews
# and fetchDealers. Now I will implement a method to access
# these from the Django app above
def get_request(endpoint, **kwargs):
    # Add code for get requests to back end
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"
    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Error: {e}")


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Error: {e}")


def add_review(request):
    if not request.user.is_anonymous:
        data = json.loads(request.body)
        try:
            # response = 
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            # Hata mesajini istege bagli olarak loglayabilirsiniz
            print(f"Error: {e}")
            return JsonResponse({
                "status": 401, 
                "message": "Error in posting review"
            })
    else:
        return JsonResponse({
            "status": 403, 
            "message": "Unauthorized"
        })
