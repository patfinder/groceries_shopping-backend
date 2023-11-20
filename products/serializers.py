from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):  # new
    owner = serializers.ReadOnlyField(source="owner.username")
    # highlight = serializers.HyperlinkedIdentityField(  # new
    #     view_name="product-highlight", format="html"
    # )

    class Meta:
        model = Product
        fields = '__all__'
