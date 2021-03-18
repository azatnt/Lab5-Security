# Generated by Django 3.1.7 on 2021-03-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DAddressType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'd_address_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DIdcardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'd_idcard_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DPhoneType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'd_phone_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'd_regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 't_addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TDebtData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agr_num', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('close_date', models.DateField()),
                ('overdue_day', models.CharField(max_length=255)),
                ('loan_amount', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('claim_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('claim_amount', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('main_debt', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('percentage_debt', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('fine_debt', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('indebt_debt', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 't_debt_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TIdcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcard_num', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('given_by', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 't_idcard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPersons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=200)),
                ('iin', models.CharField(max_length=12)),
                ('full_name', models.CharField(max_length=500)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('desc', models.TextField()),
                ('id_rollback', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('client_code', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 't_persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPhones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 't_phones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=500)),
                ('bin', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
            options={
                'db_table': 't_work',
                'managed': False,
            },
        ),
    ]