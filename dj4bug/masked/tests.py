from django.test import TestCase
from .models import ModelB


class TestModelB(TestCase):
    def test_query_order_by_ref(self):
        list(ModelB.objects.order_by('ref'))
