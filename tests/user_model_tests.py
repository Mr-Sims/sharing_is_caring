from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(
            email='test@abv.bg',
        )
        self.user.set_password = '1234567890Mazen'
        self.user.save()

    def test_UserInit(self):
        self.assertEqual('test@abv.bg', self.user.email)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)