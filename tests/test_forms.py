from django.contrib.auth import get_user_model
from django.test import TestCase

from sharing_is_caring.profiles.forms import UserProfileForm
from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class ProfileFormTest(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='Maznaparola1234')

    def test_ProfileCreate_expectTrue(self):
        user = UserModel.objects.create(email='test1@abv.bg', password='Maznaparola1234')
        profile = UserProfile(
            user=user,
        )
        profile.save()
        profile_form = UserProfileForm(
            {'first_name': 'test',
             'last_name': 'test',
             'address': 'testaddress',
             'city': 'testcity',
             'gender': 'male',
             'number_of_children': 3,
             'image': '/path/to/img.jpg',
             'user_id': 1,
             'is_complete': 'True'
             }
        )
        self.assertTrue(profile_form.is_valid())

    def testProfileFormSave__whenValid(self):
        data = {'first_name': 'test',
                'last_name': 'test',
                'address': 'testaddress',
                'city': 'testcity',
                'gender': 'male',
                'number_of_children': 3,
                'image': '/path/to/img.jpg',
                'user_id': 1,
                'is_complete': 'True'
                }
        form = UserProfileForm(data)
        self.assertTrue(form.is_valid())

    def testProfileFormInValid__whenInValid(self):
        data = {'first_name': 'test12',
                'last_name': 'test1212',
                'address': 'testaddress1212',
                'city': 'testcity1212',
                'gender': 'male12',
                'number_of_children': 1,
                'image': '/path/to/img.jpg',
                'user_id': 1,
                'is_complete': 'True'
                }
        form = UserProfileForm(data)
        self.assertFalse(form.is_valid())

