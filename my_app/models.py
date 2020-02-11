from django.contrib.auth.models import User
from django.db import models

STATE_CHOICE = (
    ('CE', 'Ceara'),
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('RS', 'Rio Grande do Sul')
)


class Address(models.Model):
    address = models.CharField(max_length=255)
    address_complement = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICE)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '%s %s %s' % (self.address, self.city, self.state)
