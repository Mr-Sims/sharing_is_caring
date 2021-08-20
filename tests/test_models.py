from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from sharing_is_caring.main_content.models import Post
from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class UserProfileModelTest(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='1234')

    def test_profileCreate_whenInvalidNameAddressCity_shouldRaiseException(self):
        profile = UserProfile.objects.get(
            user_id=self.user.id,
        )
        profile.first_name = '1234'
        profile.last_name = '1234'
        profile.address = '1234'
        profile.city = '1 2 3 4 '
        profile.number_of_children = 1
        profile.gender = 'male'
        profile.is_complete = True
        try:
            profile.full_clean()
            profile.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_profileCreate_whenValidNameAddressCity_shouldCreateIt(self):
        profile = UserProfile.objects.get(
            user_id=self.user.id,
        )
        profile.first_name = 'testname'
        profile.last_name = 'testname'
        profile.address = 'testaddress'
        profile.city = 'testcity'
        profile.number_of_children = 1
        profile.gender = 'male'
        profile.is_complete = True

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile)


class PostModelTest(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='1234')

    def test_postCreate__whenValidName_shouldCreate(self):
        post = Post(
            name='test',
            description='test',
            item_type='Toy',
            condition='Used',
            type='Search',
            image='/path/to/img.jpg',
            user_id=self.user.id,
        )
        post.full_clean()
        post.save()

        self.assertIsNotNone(post)


    def test_postCreate__whenInvalidName_shouldRaise(self):
        post = Post(
            name='1 2 3 4 $',
            description='test',
            item_type='Toy',
            condition='Used',
            type='Search',
            image='/path/to/img.jpg',
            user_id=self.user.id,
        )
        try:
            post.full_clean()
            post.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)
