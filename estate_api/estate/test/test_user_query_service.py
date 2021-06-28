from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from estate.models import Status, Property, StatusHistory
from estate.serializers import StatusHistorySerializer
import datetime
import pytz

PROP_URLS = reverse('estates:userfilter')


def create_test_status():
    all_status = [Status.objects.create(name="pre_venta"),
                  Status.objects.create(name="en_venta"),
                  Status.objects.create(name="vendido"),
                  Status.objects.create(name="comprado")]
    return all_status


def create_property(**params):
    default_property = {
        "address": "1938 Sullivan Place",
        "city": "Metropolis ",
        "price": 500000
    }
    default_property.update(params)
    return Property.objects.create(**default_property)


class UserEstateQuery(TestCase):
    """Test the user can get estates by conditions"""

    def setUp(self):
        self.client = APIClient()
        self.all_status = create_test_status()

    def test_retrieve_allowed_status(self):
        """Test method brings only allowed status"""
        property1 = create_property(address="1007 Mountain Drive")
        property2 = create_property()
        StatusHistory.objects.create(update_date=datetime.
                                     datetime(2015, 5, 21, 20, 8, 7, 127325,
                                              tzinfo=pytz.UTC),
                                     property=property1,
                                     status=self.all_status[-1])
        StatusHistory.objects.create(update_date=datetime.
                                     datetime(2015, 5, 21, 20, 8, 7, 127325,
                                              tzinfo=pytz.UTC),
                                     property=property1,
                                     status=self.all_status[0])
        StatusHistory.objects.create(update_date=datetime.
                                     datetime(2015, 5, 21, 20, 8, 7, 127325,
                                              tzinfo=pytz.UTC),
                                     property=property2,
                                     status=self.all_status[-1])

        response = self.client.get(PROP_URLS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filters_on_existing_properties(self):
        """Test filtering estates by fields"""

        property1 = create_property()
        property2 = create_property(address="1007 Mountain Drive ",
                                    city="NY",
                                    year=2021)
        StatusHistory.objects.create(update_date=datetime.
                                     datetime(2015, 5, 21, 20, 8, 7, 127325,
                                              tzinfo=pytz.UTC),
                                     property=property1,
                                     status=self.all_status[0])
        historyvalidate = \
            StatusHistory.objects.create(
                update_date=datetime.datetime(2015, 5, 21, 20, 8, 7, 127325,
                                              tzinfo=pytz.UTC),
                property=property2,
                status=self.all_status[1])

        res = self.client.get(
            PROP_URLS,
            {'city': f'{property2.city}',
             'year': f'{property2.year}',
             'status': self.all_status[1].id}
        )

        serializer1 = StatusHistorySerializer(historyvalidate)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertIn(serializer1.data, res.data)

    def test_filter_not_found_elements(self):
        property1 = create_property()
        StatusHistory.objects.create(
            update_date=datetime.datetime(2015, 5, 21, 20, 8, 7, 127325,
                                          tzinfo=pytz.UTC),
            property=property1,
            status=self.all_status[0])

        res = self.client.get(
            PROP_URLS,
            {'city': f'{property1.city}',
             'status': self.all_status[-1].id}
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 0)
