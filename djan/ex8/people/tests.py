
from django.test import TestCase
from .views import link_child_to_parent
from django.urls import reverse
from rest_framework import status
from .models import Person, Parent
import json
from django.test import Client

class PersonTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(id_number='400', name="yarden", birth_date="2000-01-01", city="Tel Aviv")
       
    def test_is_adult(self):
        person = Person.objects.create(
            id_number=2,
            name="jordan",
            birth_date="2010-01-01",
            city="Rishon Letzion",
        )
        self.assertFalse(person.is_adult())

class ParentTestCase(TestCase):
    def setUp(self):
        client = Client()
        child1 = Person.objects.create(id_number=1, name="Child 1", birth_date="2000-01-01", city="Los Angeles")
        child2 = Person.objects.create(id_number=2, name="Child 2", birth_date="2005-01-01", city="Los Angeles")
        child3 = Person.objects.create(id_number=3, name="Child 3", birth_date="2010-01-01", city="Los Angeles")
        self.parent = Parent.objects.create(id_number=456, name="Jane Smith", birth_date="1980-01-01", city="Los Angeles", workplace="google", base_salary=60000)
        self.parent.children.set([child2, child3])

    
    def test_create_or_list_parents(self):
        data = {
            "id_number": 1,
            "name": "New Parent",
            "birth_date": "1990-03-03",
            "city": "New City",
            "workplace": "amducs",
            "base_salary": 39000,
            "children": [1]
        }
        response = self.client.post(reverse('create_or_list_parents'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.content.decode(), "Parent added successfully")

    def test_link_child_to_parent(self):
        data= {
            "parent_id": 456,
            "child_id": 2
        }
        response = self.client.post(reverse('link_child_to_parent'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        parent = Parent.objects.get(id_number=456)
        self.assertTrue(parent.children.filter(id_number=2).exists())

    def test_rich_children(self):
        response = self.client.post(reverse('rich_children'))
        self.assertEqual(response.status_code, 400)

    def test_find_parents(self):
        response = self.client.post(reverse('find_parents'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_retrieve_children_of_parent(self):
        response = self.client.get(reverse('retrieve_children_of_parent', kwargs={'parent_id': 456}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) > 0)
 

    def test_find_grandparents(self):
        response = self.client.get(reverse('find_grandparents', kwargs={'person_id': 1}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) > 0)


    








