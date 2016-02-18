from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from questions.models import Question
from rest_framework.test import APIClient


class QuestionTest(APITestCase):

    def setUp(self):
        """
        Create a new user
        """
        self.superuser = User.objects.create_superuser('nirgoldman', 'nir@goldman.com', '1234')
        self.client.login(username='nirgoldman', password='1234')


    def test_CRUD_entity_of_question(self):
        """
        Ensure we can create a new question object.-the problem that we need user to authorize for post data
        """

        #AUTH
        client = APIClient(enforce_csrf_checks=True)
        client.login(username='nirgolman', password='1234')

        #CREATE
        url = reverse("questions")
        data = {"title": "Do you like programming?", "description": "Lorem", "author": 1}
        self.client.post('/questions', data, dataformat='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #READ
        url = '/questions/1/'
        data = {"id": 1, "title": "Do you like programming?", "description": "Lorem", "author": 1}
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.data, data)
        self.assertEqual(Question.objects.count(), 1)



        #UPDATE
        url = '/questions/1/'
        data = {"title": "Do you like Python?", "description": "Ipsum", "author": 1}
        self.client.put('/questions/1/', data, dataformat='json')
        data = {"id": 1, "title": "Do you like Python?", "description": "Ipsum", "author": 1}
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.data, data)


        #DELETE
        self.client.delete("/questions/1/", data=data)
        self.assertEqual(Question.objects.count(), 0)

        client.logout()

    def test_check_url(self):
        """
        Check the url
        """
        # check if url exist--works
        url = reverse("questions")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


