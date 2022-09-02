from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import http404
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authenticatio_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    # We can use perform insted of put()
    # we can use it in mixen it allowed

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
            print(content)
        serializer.save(content=content)
        # serializer.save(user=self.request.user)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = pk


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsStaffEditorPermission]

    # def get(request, *args, **kwargs):
    #     queryset = Product.objects.all().last()
    #     ser = {}
    #     ser['id'] = queryset.id
    #     ser.update(ProductSerializer(queryset).data)
    #     print(ser)
    #     return Response(ser)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        serializer.save(content=instance.content)


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# Here using mixin with class baseviews


class ProductMixinView(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content is None:
            content = title
        serializer.save(content=content)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk is None:
            # Retrieve same as detail we use mixen with list
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     data = request.data
    #     serialized = ProductSerializer(data=data)
    #     if serialized.is_valid(raise_exception=True):
    #         title = serialized.validated_data.get('title')
    #         content = serialized.validated_data.get('content') or None
    #         if content is None:
    #             content = title
    #             serialized.save(content=content)
    #     return Response({'status': 'bad data'})


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     return Http404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
                serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid': 'Not good data'}, status=400)
