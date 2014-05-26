#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from feeds.views import OptionsView
from feeds.models import Options


class ViewsLoggedInTest(TestCase):
    """
    Test Options views for users that are authenticated.
    """

    username = "john"
    realname = "John Lennon"
    password = "password"

    def setUp(self):
        """
        Set up enivironment to test models
        """
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
            self.username,
            self.realname,
            self.password
        )
        self.user.save()
        """Test user."""

    def test_options_anonymous(self):
        """
        Try to view options as anonymous.
        """
        client = Client()
        response = client.get(reverse('planet:options'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=%s' % (reverse('planet:options'))
        )

    def test_options_user(self):
        """
        Try to view options as anonymous.
        """
        request = self.factory.get(reverse('planet:options'))
        request.user = self.user
        response = OptionsView.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_options_post(self):
        """
        Try to view options as anonymous.
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(
            reverse('planet:options'),
            {
                'number_initially_displayed': "11",
            },

        )
        self.assertEquals(response.status_code, 200)

        """
        .. todo:: This should actually be '11', after
        we updated the value above.
        """
        options = Options.objects.get(user=self.user)
        self.assertEqual(options.user, self.user)
        self.assertEqual(options.number_initially_displayed, 11)
