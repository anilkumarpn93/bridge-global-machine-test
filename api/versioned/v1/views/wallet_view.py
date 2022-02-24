from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.versioned.v1.managers.wallet_manager import WalletManager


class WalletBalanceApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        manager = WalletManager(request.user)
        return Response(manager.balance())

    def post(self, request):
        manager = WalletManager(request.user)
        return Response(manager.enable())

    def patch(self, request):
        manager = WalletManager(request.user)
        return Response(manager.disable())


class WalletDepositApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['withdrawn_by'] = request.user.customer_xid
        manager = WalletManager(request.user, request)
        return Response(manager.withdraw(data))


class WalletWithdrawalApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['withdrawn_by'] = request.user.customer_xid
        manager = WalletManager(request.user, request)
        return Response(manager.withdraw(data))




