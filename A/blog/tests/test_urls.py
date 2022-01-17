from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import all_posts, post_detail


class TestUrls(SimpleTestCase):
    def test_all_post(self):
        url = reverse('blog:all_posts')
        self.assertEqual(resolve(url).func, all_posts)
