# Service-Strassenverkehrsamt
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