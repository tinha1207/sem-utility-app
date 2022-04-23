Backend

Made of 2 services:

- File Upload Service

  - Dependencies:
    - Python 3.9+
    - To install dependencies -> $ pipenv install
  - To Launch
    - cd to ./iso_keyword
    - run dev script -> $ pipenv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
    - run production scrpt -> $ pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8001

- Resources Service
  - Dependencies:
    - Python 3.9+
    - To install dependencies -> $ pipenv install
  - To Launch
    - cd to ./resources
    - run dev script -> $ pipenv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
    - run production script -> $ pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8002
