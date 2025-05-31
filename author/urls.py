# Create your urls here
#
# from django.urls import path, include
# from rest_framework import routers
#
# from author.views import AuthorViewSet
#
# author_list = AuthorViewSet.as_view(actions={
#            "get": "list",
#            "post": "create",
#        })
# author_detail = AuthorViewSet.as_view(actions={
#            "get": "retrieve",
#            "put": "update",
#            "patch": "partial_update",
#            "delete": "destroy",
#        })
#
# urlpatterns = [
#    path("author/", author_list, name="manage-list"),
#    path("author/<int:pk>/", author_detail, name="author-detail"),
# ]
#
# app_name = "author"
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register(r'', AuthorViewSet,
                basename="manage")

urlpatterns = [
    path("author/", include(router.urls)),
]
