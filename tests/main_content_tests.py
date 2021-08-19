from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sharing_is_caring.main_content.models import Post

UserModel = get_user_model()


class PostsCreateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@abv.bg', password='1234567890Mazen')

    def test__whenNewPostCreated__expectNothing(self):
        self.client.force_login(self.user)
        post = Post.objects.create(
            name='test_name',
            description='test_description',
            item_type='Toy',
            condition='Used',
            type='Search',
            image='path/to/image.png',
            user_id=self.user.id
        )
        response = self.client.get(reverse('post details', kwargs={
            'pk': post.id
        }))
        p = response.context['post']
        self.assertEqual(p.id, 1)
        self.assertEqual(200, response.status_code)

