"""
API URL Configuration.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListView.as_view(), name="blogpost-view-create"),
]

