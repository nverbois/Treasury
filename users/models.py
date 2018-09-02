from django.db import models
from django.contrib.auth.models import AbstractUser
from bank.models import Transaction

# Create your models here.
class Kot(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.year)

class CustomUser(AbstractUser):
    # add additional fields in here
    treasurer = models.BooleanField(default = False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.get_full_name()

    def get_balance(self):
        listOfTransactions = Transaction.objects.filter(user=self)
        balance = 0
        for t in listOfTransactions:
            if t.positive:
                balance += t.cost
            else:
                balance -= t.cost
        return balance