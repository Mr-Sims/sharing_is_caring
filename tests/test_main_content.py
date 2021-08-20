from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sharing_is_caring.main_content.models import Post

UserModel = get_user_model()


class PostsViewsTests(TestCase):
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
        self.assertEqual(p.user_id, self.user.id)

        # owner = response.context['is_owner']
        # self.assertEqual(owner, self.user.id)
        self.assertEqual(200, response.status_code)

    def test_whenPostIsDeleted__expectNothing(self):
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
        post.delete()
        # self.assertEqual(p.id, 1)
        self.assertEqual(p.user_id, self.user.id)
        self.assertEqual(200, response.status_code)

    def test_whenPostUpdate__expectNothing(self):
        self.client.force_login(self.user)
        post = Post.objects.create(
            name='testname',
            description='testdescription',
            item_type='Toy',
            condition='Used',
            type='Search',
            image='path/to/image.png',
            user_id=self.user.id
        )
        response = self.client.post(
            reverse('update post', kwargs={'pk': post.id}),
            {'name': 'testupdate',
             'description': 'testdescription',
             'item_type': 'Toy',
             'condition': 'Used',
             'type': 'Search',
             'image': 'path/to/image.png',
             'user_id': 'self.user.id'
             })

        self.assertEqual(response.status_code, 302)

        post.refresh_from_db()
        self.assertEqual(post.name, 'testupdate')

    def test_whenUserCommentsOnAnotherUser_expectNothing(self):
        self.user2 = UserModel.objects.create_user(email='test2@abv.bg', password='1234567890Mazen')
        self.client.force_login(self.user)


