from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User


class TestImage(TestCase):
    def setUp(self):
        self.user = User(username='charles')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)
