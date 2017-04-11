#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4

"""
Serializers for the Feeds API
"""

from rest_framework import serializers
from category.models import Category

from ..models import Options, WebSite, Feed, Post


class OptionsSerializer(serializers.ModelSerializer):
    """
    Serializer for User Options

    .. classauthor:: Andreas Neumeier
    """
    class Meta:
        model = Options
        fields = (
            "pk",
            "number_initially_displayed",
        )


class FeedBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            'pk',
            'name',
        )


class WebSiteSerializer(serializers.HyperlinkedModelSerializer):
    feeds = FeedBriefSerializer(
        required=True,
        many=True
    )

    class Meta:
        model = WebSite
        fields = (
            'pk',
            'name',
            'url',
            'slug',
            'feeds',
        )
        extra_kwargs = {
            'name': {
                'view_name': 'planet:website-detail',
                'lookup_field': 'pk'
            },
        }


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            'pk',
            'url',
            'get_absolute_url',
            'website',
            'feed_url',
            'name',
            'short_name',
            'slug',
            'is_active',
            'errors',
            'category',
            'title',
            'link',
            'tagline',
            'language',
            'copyright',
            'author',
            'webmaster',
            'pubDate',
            'last_modified',
            'ttl',
            'image_title',
            'image_link',
            'image_url',
            'etag',
            'last_checked',
            'check_interval',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'feed',
            'title',
            'link',
            'published',
        )


class UserOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Options
        fields = (
            'pk',
            'user',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'url', )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('name', )
