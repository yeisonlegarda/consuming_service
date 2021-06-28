from django.db import models


class Property(models.Model):
    """Model for property table"""
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=32)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'property'

    def __str__(self):
        return f'{self.address} {self.city}'


class Status(models.Model):
    """Model for status table"""
    name = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=64)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return f'{self.id} {self.name}'


class StatusHistory(models.Model):
    """
    Status history relates status and property has got all status given
    to a property
    """
    property = models.ForeignKey('Property', models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        db_table = 'status_history'

    def __str__(self):
        return f'{self.id} ' \
               f'{self.property.address} ' \
               f'{self.status.name} ' \
               f'{self.update_date}'
