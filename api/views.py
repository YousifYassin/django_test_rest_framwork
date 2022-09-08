# import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(
            model_data,
            fields=["id", "title", "price", "sale_price"],
        )
        # # json_data_str = json.dumps(data)
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # data = ProductSerializer(model_data).data

    return JsonResponse(data)


@api_view(["GET", "POST"])
def vi(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(
            model_data, fields={"id", "title", "price", "sale_price", "discount"}
        )
        # sale_price and discount not working need for serialzer method
    return Response(data)


@api_view(
    [
        "Post",
    ]
)
def vi_ser(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        # instance = Product.objects.all().order_by('?').first()
        # data = {}
        # if instance:
        #     data = ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
