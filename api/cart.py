from rest_framework.decorators import api_view, permission_classes
from .models import Product,Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

 #api cart
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_view(request):
    if request.method == 'POST':
        product = Product.objects.get(id=request.data['product'])
        cart_item = Cart.objects.create(user=request.user, product=product, quantity=request.data['quantity'])
        return Response({'message': 'Item added to cart'}, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)
