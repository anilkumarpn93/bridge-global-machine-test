from rest_framework.views import APIView
from rest_framework.response import Response
from api.versioned.v1.serializers.auth_serializer import AuthSerializer
from api.versioned.v1.serializers.wallet_serializer import WalletSerializer
from api.models import Wallet


class Authentication(APIView):
    def post(self, request):
        # Check the user is valid, If yes generate token
        auth_serializer = AuthSerializer(data=request.data)
        auth_serializer.is_valid(raise_exception=True)
        token = auth_serializer.generate_token()
        owned_by = auth_serializer.validated_data['customer_xid']

        # Check the wallet for the user is initialized or not
        wallet = Wallet.objects.filter(owned_by=owned_by).first()
        if not wallet:
            self.initialize_wallet(owned_by)

        # Response
        return Response({
            "token": str(token)
        })

    @staticmethod
    def initialize_wallet(owned_by):
        # Initialize wallet account
        init_data = {
            "status": Wallet.Status.ENABLED,
            "balance": 0,
            "owned_by": owned_by
        }
        wallet_serializer = WalletSerializer(data=init_data)
        wallet_serializer.is_valid(raise_exception=True)
        return wallet_serializer.save()
