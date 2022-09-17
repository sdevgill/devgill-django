from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    # Unit test to check Post model's content
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.slug, "a-good-title")
        self.assertEqual(self.post.get_read_time(), "1 min")
        # self.assertEqual(self.post.get_absolute_url(), "/a-good-title/") add this after blog is subdomain
        self.assertEqual(self.post.get_absolute_url(), "/blog/a-good-title/")

    # Unit tests to check blog urls and views
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blog/a-good-title/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "blog.html")

    def test_post_detailview(self):
        response = self.client.get(
            reverse("blog_post", kwargs={"slug": self.post.slug})
        )
        no_response = self.client.get("/blog/does-not-exist/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "blog_post.html")
