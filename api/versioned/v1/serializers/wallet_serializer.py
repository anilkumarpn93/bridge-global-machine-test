from rest_framework import serializers
from api.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'owned_by', 'status', 'enabled_at', 'balance')

    def initialize_wallet(self):
        self.is_valid(raise_exception=True)
        return self.save()

