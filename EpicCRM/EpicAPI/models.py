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
    is_staff = True


    def __str__(self):
        return "{} ({})".format(self.username, self.role)


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL, null=True,
                                        blank=True)
    existing_client = models.BooleanField(help_text="True if client with active or past\
                                          events, False is not")

    def __str__(self):
        return "Client n°{} {} {}".format(self.id, self.first_name, self.last_name)

class Contract(models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL, null=True,
                                        blank=True)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(help_text="True if signed, False if not signed")
    amount = models.FloatField(help_text="Montant du contrat en euros")
    payment_due = models.DateTimeField()
    # need to add foreign key towards Event ?

class Event(models.Model):

    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL, null=True,
                                        blank=True)
    event_status = models.BooleanField(help_text="True if ongoing, False if over")
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=1000)
