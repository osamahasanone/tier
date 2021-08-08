# URL Shortener 

A Django Rest Framwork simple API for shortening long URLs. URLs and their visit history will be saved in a MySQL database.

## Built With

The below languages, libraries and tools have been used:
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [MySQL](https://www.mysql.com/)
* [Pytest](https://docs.pytest.org/en/6.2.x/)
* [Docker](https://www.docker.com/)
* [Swagger](https://swagger.io/)

## Prerequisites

Please make sure that you have Git and Docker installed on you machine.

## Installation

1.  Clone the repo
   
```sh
git clone https://github.com/osamahasanone/tier.git
```
   
2. Build Docker images and start containers in one command:
   
```sh
docker-compose up
```

<!-- USAGE EXAMPLES -->
## Usage

Open [localhost](http://localhost:8000/) and a Swagger interface will be displayed.

### Shorten a URL

#### Request

`POST /urls/shorten`

    curl -X POST "http://localhost:8000/urls/shorten" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: iUjf62EkNHQC29J3bTMPLvmb2qniOVP7Kal7NLEUanYpWXKvjPEKjO9TlyBvd0Tf" -d "{  \"long_text\": \"YOUR_LONG_URL"}"

#### Response

It could be one of the followings:

1. **201 Created**

Long URL is not found in the database, it has been created, shortened and returned
    
    {
      "id": 1,
      "long_text": "YOUR_LONG_URL",
      "short_text": "https://tier.app/pfGrmg",
      "visits_count": 1
    }
    
2. **200 OK**
  
The long URL is already in the database, short URL has been just returned

    {
      "id": 1,
      "long_text": "YOUR_LONG_URL",
      "short_text": "https://tier.app/pfGrmg",
      "visits_count": 2
    }  
   
3. **400 Bad Request**	

No valid URL in the request    
  
    {
      "long_text": [
      "Enter a valid URL."
      ]
    }
