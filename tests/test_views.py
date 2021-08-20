from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class TestViews(TestCase):
    def test_shouldShowSignUpPage(self):
        response = self.client.get(reverse('sign up'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'auth/sign-up.html')

    def test_shouldShowSignInPage(self):
        response = self.client.get(reverse('sign in'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'auth/sign-in.html')

    def test_shouldShowLandingPage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'common/index.html')

    def test_shouldShowListPostsPage(self):
        response = self.client.get(reverse('list items'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'common/list_posts.html')

    def test_shouldShowListPostsSearchingPage(self):
        response = self.client.get(reverse('list needed items'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'common/list_posts_needed.html')

    def test_shouldShowListPostsGiveAwayPage(self):
        response = self.client.get(reverse('list give-away items'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'common/list_posts_give_away.html')

    def test_shouldShowAboutUsPage(self):
        response = self.client.get(reverse('about us'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'common/about-us.html')

    def test_shouldSignUpUser_AutoLoggin_redirectToIndex(self):
        self.user = {
            'email': 'test@abv.bg',
            'password1': 'Maznaparola1',
            'password2': 'Maznaparola1'
        }
        response = self.client.post(reverse('sign up'), self.user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

