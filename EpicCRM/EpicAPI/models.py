from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EpicTeamMember(AbstractUser):
    # Classe à partir de laquelle seront dérivés les trois teams
    """
    id
    pourrait plutôt mettre comme le suggère alex une propriété teams que pourrait remplir 
    avec trois choix, ManagerTeam, SupportTeam, SalesTeam
    """
    pass

class ManagerTeam(EpicTeamMember):
    pass

class SupportTeam(EpicTeamMember):
    pass

class SalesTeam(EpicTeamMember):
    pass


class Event:
    """
    id
    client
    date_created
    date_updated
    support_contact
    event_status
    attendees
    event_date
    notes
    """
    pass

class Client:
    """
    id
    first_name
    last_name
    email
    phone
    mobile
    company_name
    date_created
    date_updated
    sales_contact
    boolean avec si client potentiel ou existant - genre existing_client
    """
    pass

class Contract:
    """
    id
    sales_contact
    client
    date_created
    date_updated
    status
    amount
    payment_due
    """
    pass