# from django.test import TestCase

# Create your tests here.
# from django.core.urlresolvers import reverse


from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from ..views import new_topic, BoardListView
from ..models import Board
from django.contrib.auth.models import User
from ..views import new_topic, BoardListView
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
#        url = reverse('home')
#        response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)
