from rest_framework import serializers
from .models import Company, Supplier, BankAccount

class CompanySerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all(), required=False)
    bank_accounts = serializers.PrimaryKeyRelatedField(many=True, queryset=BankAccount.objects.all(), required=False)

    class Meta:
        model = Company
        fields = [
            'company_id',
            'company_name',
            'company_phone',
            'company_email',
            'company_address',
            'suppliers',
            'bank_accounts',
        ]

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'supplier_id',
            'company',
            'supplier_name',
            'dob',
            'gender',
            'phone',
            'supplier_address',
        ]

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            'bank_id',
            'company',
            'holder_name',
            'account_number',
            'bank_name',
            'branch_name',
            'swift_code',
        ]
