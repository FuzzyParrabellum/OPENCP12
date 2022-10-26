from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EpicTeamMember(AbstractUser):

    MANAGER = 'MANAGER'
    SUPPORT = 'SUPPORT'
    SALES = 'SALES'

    ROLE_CHOICES = (
        (MANAGER, 'ManagerTeamMember'),
        (SUPPORT, 'SupportTeamMember'),
        (SALES, 'SalesTeamMember')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES,
                            verbose_name="Epic Events Team's Choice")


# class Client(models.Model):

#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField()
#     phone = models.CharField(20)
#     mobile = models.CharField(20)
#     company_name = models.CharField(250)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                         on_delete=models.SET_NULL)
#     existing_client = models.BooleanField(help_text="True if client with active or past\
#                                           events, False is not")

# class Contract(models.Model):

#     sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                         on_delete=models.SET_NULL)
#     client = models.ForeignKey(Client, null=False, on_delete=models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(help_text="True if paid, False if payment pending")
#     amount = models.FloatField()
#     payment_due = models.DateTimeField()
#     # need to add foreign key towards Event ?

# class Event(models.Model):

#     client = models.ForeignKey(Client, null=False, on_delete=models.SET_NULL)
#     contract = models.ForeignKey(Contract, null=False, on_delete=models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                         on_delete=models.SET_NULL)
#     event_status = models.BooleanField(help_text="True if ongoing, False if over")
#     attendees = models.IntegerField()
#     event_date = models.DateTimeField()
#     notes = models.TextField(max_length=1000)
