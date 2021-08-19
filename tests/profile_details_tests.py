from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='1234')

    def test_getDetails__whenNewUserCreated_shouldGetProfileCreatedAndGetDetails(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))

        self.assertEqual(200, response.status_code)
        profile = response.context['profile']
        self.assertEqual(self.user.id, profile.user_id)
        posts = list(response.context['posts'])
        self.assertListEqual(posts, [])

    def test_getProfileDetails__whenNewUserLoggedIn__shouldGetNoProfileData(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))

        profile = response.context['profile']
        self.assertEqual(profile.first_name, '')
        self.assertEqual(profile.last_name, '')
        self.assertEqual(profile.address, '')
        self.assertEqual(profile.city, '')
        self.assertEqual(profile.gender, '')
        self.assertEqual(profile.number_of_children, None)
        self.assertFalse(profile.is_complete)

    def test_getProfileDetails__whenUserLoggedInWithProfileComplete__shouldGetProfileData(self):
        self.client.force_login(self.user)

        profile = UserProfile(
            user_id=self.user.id,
            first_name='test_first_name',
            last_name='test_last_name',
            address='test_address',
            city='test_city',
            gender='Male',
            number_of_children=3,
        )

        self.assertEqual(profile.first_name, 'test_first_name')
        self.assertEqual(profile.last_name, 'test_last_name')
        self.assertEqual(profile.address, 'test_address')
        self.assertEqual(profile.city, 'test_city')
        self.assertEqual(profile.gender, 'Male')
        self.assertEqual(profile.number_of_children, 3)
