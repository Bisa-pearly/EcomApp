from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from EcomApp.models import Product
from EcomApp.serializers import ProductSerializer


class ListCreateProductAPIView(APIView):
    def get(self, request):
        #products = Product.objects.all().filter(price__gte=10)
        products=Product.objects.raw("select * from EcomApp_Product where price BETWEEN 0 AND 21")
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=200)
        # return Response ({"products": products})

    def post(self, request):
        data = request.data
        # product = Product.objects.create(
        # name=data['name'],
        # price=data['price'],
        # description=data['description'],
        #        )
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=400)
        decoded_data.save()

        return Response(decoded_data.data, status=201)

        #return Response ({"product": product}) to add serilaxer we removed the parameter
        #return Response()
