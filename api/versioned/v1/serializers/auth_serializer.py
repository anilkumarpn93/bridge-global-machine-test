from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class AuthSerializer(serializers.Serializer):

    customer_xid = serializers.CharField(max_length=200)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        customer_xid = attrs.get('customer_xid')
        if customer_xid:
            user = User.objects.filter(customer_xid=customer_xid).first()
            if user:
                attrs['user'] = user
                return attrs
            else:
                msg = "Invalid customer xid."
                raise serializers.ValidationError({"customer_xid": msg}, code='authorization')
        else:
            msg = "Customer xid is required."
            raise serializers.ValidationError(msg, code='authorization')

    def generate_token(self):
        # Create access token
        token, created = Token.objects.get_or_create(user=self.validated_data['user'])
        return token.key
