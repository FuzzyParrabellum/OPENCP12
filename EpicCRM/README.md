# OPENCP12

## Presentation - EpicCRM app -

Built with **the intent of using Django Admin as a CRM** for an Event-Making Company,
EpicAdmin. Three teams co-exist in this company, each with a dedicated role, SUPPORT,
SALES and MANAGER. When added to one of these teams, an user will join the team's
django group and have all the shared permissions of that group.
Each user will be able to interact with three models, **Contracts**, **Clients** and **Events**.

Object-level permissions were included by modifying the project's **admin.py** file :

A MANAGER user will have all permissions including user creation and deletion, a SALES
user will be able to create Contracts and Clients but only modify the ones he is related to, a SUPPORT user will only have view access to Contracts and Clients and will
be able to create Events and modify the ones he is related to.

A **RESTful API was also built with DRF** in this project, with basic authentification and CRUD operations.
Object-level permissions were also enforced (see **permissions.py**).


## Requirements

After cloning the project, and activating a virtual environment, install all dependencies from **requirements.txt** with:
'''
pip install -r requirements.txt
'''
Then install **postgresql** if not already done and configure a database with these
settings as written in settings.py :
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'epiccrm_db',
        'USER': 'user1',
        'PASSWORD': 'epic_Passw0rd',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
'''

## How to use

After following requirements, enter the EpicCRM project folder and run the server with:
'''
python manage.py runserver
'''

Then go to this endpoint to create your first user and use the CRM afterwards:
http://127.0.0.1:8000/admin/

### Use the api with these endpoints:
(you will need to authentify yourself first at http://127.0.0.1:8000/api-auth/login/
by passing your **username** and your **password**)

* http://127.0.0.1:8000/api/EpicTeamMember/
* http://127.0.0.1:8000/api/Client/
* http://127.0.0.1:8000/api/Contract/
* http://127.0.0.1:8000/api/Event/



