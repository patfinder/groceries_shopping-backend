from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
    # path(
    #     "products/<int:pk>/highlight/",
    #     views.SnippetHighlight.as_view(),
    #     name="snippet-highlight",
    # ),  # new
    # path("users/", views.UserList.as_view(), name="user-list"),
    # path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
