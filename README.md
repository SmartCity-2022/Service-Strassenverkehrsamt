# Service-Strassenverkehrsamt

"Service-Strassenverkehrsamt" is a microservice of the "SmartCity"-Project. Here, a user is able to see registered vehicles or register new ones via requests. In addition to that, a citizen of the SmartCity will be able to create requests for new driver licenses. And finally a user is able to see open bills and penaltys.

## How to run

### Run frontend

In directory frontend:

    npm start


### Run backend

1. Create virtual environment

        pip install virtualenv

    - In directory SmartCity

            python -m venv [NAME OF VENV]

2.  Activate virtual environment

    - On Windows

            .\path\to\venv\Scripts\activate

    - On Linux

            source \path\to\venv\bin\activate.sh

3. Install required packages

    - Go to SmartCity directory
    
            pip install -r requirements.txt

4. Run Application

    - In SmartCity directory

            python manage.py runserver
            
## Run tests

1. Start backend as above.
2. Run tests
    - In SmartCity/test directory
    
            python test.py
            
3. Ensure that all needed packages as above are installed
