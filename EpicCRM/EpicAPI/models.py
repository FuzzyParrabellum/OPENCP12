from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission


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
    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return "{} {} ({})".format(self.first_name ,self.username, self.role)

    def save(self, *args, **kwargs):
        if not self.id:
            # check if the user has been created yet, if not then we are halfway
            # through the user creation form and the line below will run
            return super().save(*args, **kwargs)
        if self.groups.all().exists():
            # If the user is already in a group (then we are in edit mode), remove him 
            # from old group and move him to new group
            self.groups.clear()
            if self.role == 'MANAGER':
                self.groups.add(Group.objects.get(name='manager_team'))
            elif self.role == 'SUPPORT':
                self.groups.add(Group.objects.get(name='support_team'))
            elif self.role == 'SALES':
                self.groups.add(Group.objects.get(name='sales_team'))
            return super().save(*args, **kwargs)
        # The conditionnals below will only run after first adding a user to a group
        if self.role == 'MANAGER':
            self.groups.add(Group.objects.get(name='manager_team'))
        elif self.role == 'SUPPORT':
            self.groups.add(Group.objects.get(name='support_team'))
        elif self.role == 'SALES':
            self.groups.add(Group.objects.get(name='sales_team'))
        return super().save(*args, **kwargs)
    


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
        return "Client n°{} {} {}".format(self.id, self.first_name, self.last_name)

class Contract(models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL, null=True,
                                        blank=True)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(help_text="True if signed, False if not signed")
    amount = models.FloatField(help_text="Contract amount in euros")
    payment_due = models.DateTimeField()

    def __str__(self):
        return f"Contract #{self.id} for {self.client}"

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

    def __str__(self):
        return f"Event #{self.id} for {self.contract}"
