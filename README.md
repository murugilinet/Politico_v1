# Politico_v1

## Badges
[![Build Status](https://travis-ci.org/murugilinet/Politico_v1.svg?branch=develop)](https://travis-ci.org/murugilinet/Politico_v1)
[![Maintainability](https://api.codeclimate.com/v1/badges/36f8db0d31d86553f093/maintainability)](https://codeclimate.com/github/murugilinet/Politico_v1/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/murugilinet/Politico_v1/badge.svg)](https://coveralls.io/github/murugilinet/Politico_v1)
|

## Deployment
* Click here to view hosted application [hosted](https://politico-linet.herokuapp.com/api/v1/offices)
## Endpoints
|   METHOD       |    URl                       | FUNCTION
|  ------------  | ----------                   |  ---------
|   POST         | app/api/v1/offices           |  create an office 
|   POST         | app/api/v1/parties           |  create a party
|   GET          | app/api/v1/offices           |  find all offices
|   GET          | app/api/v1/parties           | find all parties
|   GET          | app/api/v1/offices/office_id | find a specific office with the office_id
|   GET          | app/api/v1/parties/party_id  | find a specific party with the party_id
|   DELETE       | app/api/v1/offices/office_id | delete a specific office with the office_id
|   DELETE       | app/api/v1/parties/party_id  | delete a specific party with  the party_id

## Tools Used

* Flask Restful - framework for python
* Virtual Environment - used to create an isolated python environment
* Unittest - tool for running tests

## Getting Started
* Clone the repository:
        
        `git clone https://github.com/murugilinet/Politico_v1.git`
* Change directory to the cloned folder:

        `cd Politico_v1`
* If you do not have a virtual environment installed run this to install:

        `pip install virtualenv`
* Create a virtual environment:

        `virtualenv venv`
* Activate your virtual environment:

        `source venv/bin/activate`

* Install application dependencies:

        `pip install -r requirements.txt`

* Run the application:

        `python run.py`
## Running tests
*  Install pytest while the virtual environment is active:

        `pip install pytest`
*Run the tests:

        `pytest`