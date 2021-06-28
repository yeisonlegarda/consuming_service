from django.test import TestCase
from estate import models
import pytz
import datetime


class ModelTest(TestCase):

    def test_status_model(self):
        """Test status model is created and returns str method"""
        status = models.Status.objects.create(
            name='testStatusName'
        )
        self.assertEqual(str(status), f'{status.id} {status.name}')

    def test_property_model(self):
        """Test model is up and running"""
        property = models.Property.objects.create(
            address='20 Ingram Street',
            city='NY',
            price=5000
        )
        self.assertEqual(str(property), f'{property.address} {property.city}')

    def test_status_history_model(self):
        """Test history status model works fine"""
        status = models.Status.objects.create(
            name='testStatusName'
        )
        property = models.Property.objects.create(
            address='20 Ingram Street',
            city='NY',
            price=5000
        )
        status_history = models.StatusHistory.objects.create(
            status=status,
            property=property,
            update_date=datetime.datetime(2015, 5, 21, 20, 8, 7, 127325,
                                          tzinfo=pytz.UTC)
        )
        self.assertEqual(str(status_history),
                         f'{status_history.id} '
                         f'{property.address} '
                         f'{status.name} {status_history.update_date}')
