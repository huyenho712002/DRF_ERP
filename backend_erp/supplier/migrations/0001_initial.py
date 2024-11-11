# Generated by Django 4.2.16 on 2024-11-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=15)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=255)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone', models.CharField(max_length=15)),
                ('supplier_address', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='supplier.company')),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('holder_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('swift_code', models.CharField(max_length=11)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='supplier.company')),
            ],
        ),
    ]
