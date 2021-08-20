from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sharing_is_caring.common.models import Comment
from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='Maznaparola1234')

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
            first_name='testfirstname',
            last_name='testlastname',
            address='testaddress',
            city='testcity',
            gender='Male',
            number_of_children=3,
        )

        self.assertEqual(profile.first_name, 'testfirstname')
        self.assertEqual(profile.last_name, 'testlastname')
        self.assertEqual(profile.address, 'testaddress')
        self.assertEqual(profile.city, 'testcity')
        self.assertEqual(profile.gender, 'Male')
        self.assertEqual(profile.number_of_children, 3)

    def test_whenUserUpdatesProfileDetails__expectNothing_and_is_complete_setToTrue(self):
        self.client.force_login(self.user)
        profile = UserProfile(
            user_id=self.user.id,
            first_name='testfirstname',
            last_name='testlastname',
            address='testaddress',
            city='testcity',
            gender='male',
            number_of_children=3,
            is_complete=False,
        )
        response = self.client.post(reverse('edit profile', kwargs={'pk': profile.user_id}),
                         {'first_name': 'testupdate',
                          'last_name': 'testupdate',
                          'address': 'updateaddress',
                          'city': 'updatecity',
                          'gender': 'female',
                          'number_of_children': 4,
                          'user_id': 'self.user.id'
                          })

        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()

        self.assertEqual(profile.first_name, 'testupdate')
        self.assertTrue(profile.is_complete)

    def test_whenUserCommentsOnAnotherUser_expectNothing(self):
        self.client.force_login(self.user)
        comment_receiver_user = UserModel.objects.create_user(
            email='test2@abv.bg',
            password='1234567890Mazen'
        )
        comment_receiver_profile = UserProfile.objects.get(user_id=comment_receiver_user.id)

        comment = Comment.objects.create(
            comment='test Comment',
            user_id=self.user.id,
            user_to_be_commented=comment_receiver_profile,
        )

        comment_exists = Comment.objects.filter(
            user_id=self.user.id,
            pk=comment.id,
        ).exists()
        self.assertTrue(comment_exists)
