from rest_framework import serializers
from .models import CustomUser,Product,Cart,Order,Role

#role_id
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields =['id','name']


#customer
class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = CustomUser
        fields = ['id','username','email','is_active','role']

    def create(self,validated_data):
        role_data = validated_data('role')
        role = Role.objects.get(name=role_data['name'])
        user = CustomUser(**validated_data,role=role)
        user.set_password(validated_data['password'])
        user.save()
        return user

#product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'name', 'description', 'price', 'image', 'stock']

#cart
class CartSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cart
        fields =['id','quantity','user_id','product_id']   

#order
class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Order
        fields = ['id ','total_price','status','user_id','created_at']    