from django.test import TestCase

from sharing_is_caring.user_auth.forms import SignUpForm
from sharing_is_caring.user_auth.models import SharingIsCaringUser


class SighUpTest(TestCase):

    def test_whenPasswordsDoesMatch_expectNoting(self):
        user_form = SignUpForm(
            {'email': 'test@abv.bg',
             'password1': '1234',
             'password2': '1234'
             }
        )
        self.assertTrue(user_form.is_valid())

    def test_whenPasswordsDoesNotMatch_expectRaiseValidationError(self):
        user_form = SignUpForm(
            {'email': 'test@abv.bg',
             'password1': '1234',
             'password2': '1111'
             }
        )
        self.assertFalse(user_form.is_valid())

    def test_whenEmailIsValid_expectNoting(self):
        user_form = SignUpForm(
            {'email': 'test@abv.bg',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertTrue(user_form.is_valid())

    def test_whenEmailIsNotValid_expectRaiseValidationError(self):
        user_form = SignUpForm(
            {'email': 'test.test.test',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertFalse(user_form.is_valid())

    def test_whenUserEmailAlreadyExists_expectRaiseValidationError(self):
        SharingIsCaringUser.objects.create(email='test@abv.bg', password='1234')

        user_form = SignUpForm(
            {'email': 'test@abv.bg',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertFalse(user_form.is_valid())

    def test_whenUser_withValidEmailAndPasswords(self):
        user_form = SignUpForm(
            {'email': 'test@abv.bg',
             'password1': '1234',
             'password2': '1234',
             }
        )
        self.assertTrue(user_form.is_valid())
        user_form.save()
        registered_user = SharingIsCaringUser.objects.get(email='test@abv.bg')
        self.assertIsNotNone(registered_user)


class SighInTest(TestCase):

    def test_whenUserExistAndPasswordsDoesMatch_expectNoting(self):
        user = SharingIsCaringUser.objects.create(email='test@abv.bg', password='1234')
        registered_user = SharingIsCaringUser.objects.get(email='test@abv.bg')
        self.assertTrue((registered_user is not None) and user.is_authenticated)

    def test_whenUserNot_expectRaise(self):
        user = None
        self.assertTrue((user is None))
