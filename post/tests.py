from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import DevStack


class GenericPostModelViewSetTest(APITestCase):
    '''post/views.py의 GenericPostModelViewSet이 정상적으로 동작하는지를 검증하는 테스트'''

    def setUp(self):
        ''' DevStack 생성, 회원가입 및 로그인 수행'''
        DevStack.objects.create(name="python")
        User = get_user_model()
        User.objects.create_user(
            email="test@test.com", first_name="test", last_name="user", password="0000"
        )

        self.client.login(email="test@test.com", password="0000")

    def test_posting_create(self):
        '''GenericPostModelViewSet POST 메소드 검증'''
        data = {
            "post_type": "ST",
            "meet_type": "ON",
            "location_info": "",
            "title": "test",
            "content": "test",
            "crew": [1],
            "dev_tag": [1],
        }

        response = self.client.post(reverse("post-list"), data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
