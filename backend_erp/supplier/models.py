from django.db import models
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=255)
    company_address = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Supplier(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    supplier_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="suppliers")
    supplier_name = models.CharField(max_length=255)
    dob = models.DateField(_("Date of Birth"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    supplier_address = models.CharField(max_length=255)

    def __str__(self):
        return self.supplier_name


class BankAccount(models.Model):
    bank_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="bank_accounts")
    holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.holder_name} - {self.bank_name}"
