from api.models import Wallet
from api.versioned.v1.serializers.wallet_serializer import WalletSerializer
from api.versioned.v1.serializers.withdrawal_serializer import WithdrawalSerializer
from api.versioned.v1.serializers.deposit_serializer import DepositSerializer


class WalletManager:
    user = None
    wallet = None
    request = None

    def __init__(self, user, request=None):
        self.user = user
        self.request = request

    def balance(self):
        wallet = Wallet.objects.filter(owned_by=self.user.customer_xid).first()
        serializer = WalletSerializer(wallet)
        return serializer.data

    def withdraw(self, data):
        serializer = WithdrawalSerializer(data=data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.__remove_amount_to_balance(data['amount'])
        return serializer.data

    def deposit(self, data):
        serializer = DepositSerializer(data=data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.__add_amount_to_balance(data['amount'])
        return serializer.data

    def enable(self):
        wallet = Wallet.objects.filter(owned_by=self.user.customer_xid).first()
        serializer = WalletSerializer(wallet)
        serializer.update(wallet, {"status": Wallet.Status.ENABLED})
        return serializer.data

    def disable(self):
        wallet = Wallet.objects.filter(owned_by=self.user.customer_xid).first()
        serializer = WalletSerializer(wallet)
        serializer.update(wallet, {"status": Wallet.Status.DISABLED})
        return serializer.data

    def __add_amount_to_balance(self,amount):
        wallet = Wallet.objects.filter(owned_by=self.user.customer_xid).first()
        serializer = WalletSerializer(wallet)
        serializer.update(wallet, {"balance": float(amount) + float(wallet.balance)})

    def __remove_amount_to_balance(self,amount):
        wallet = Wallet.objects.filter(owned_by=self.user.customer_xid).first()
        serializer = WalletSerializer(wallet)
        serializer.update(wallet, {"balance":  float(wallet.balance) - float(amount)})








