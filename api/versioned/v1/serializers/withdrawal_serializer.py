from rest_framework import serializers
from api.models import Withdrawal
from api.models import Wallet


class WithdrawalSerializer(serializers.ModelSerializer):
    reference_id = serializers.CharField(required=True)
    amount = serializers.CharField(required=True)

    class Meta:
        model = Withdrawal
        fields = "__all__"

    def validate_amount(self, value):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            wallet = Wallet.objects.filter(owned_by=user.customer_xid).first()
            if wallet:
                if not (0 < float(value) < float(wallet.balance)):
                    raise serializers.ValidationError("Invalid amount")
            else:
                raise serializers.ValidationError("Wallet not found for user.")
        else:
            raise serializers.ValidationError("Logged in user not found.")
        return value
