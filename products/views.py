from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers  # new
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Product
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer


# class ProductHighlight(generics.GenericAPIView):  # new
#     queryset = Product.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         product = self.get_object()
#         return Response(product.highlighted)


@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {
            # "users": reverse("user-list", request=request, format=format),
            "products": reverse("product-list", request=request, format=format),
        }
    )


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # new

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )  # new

#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
