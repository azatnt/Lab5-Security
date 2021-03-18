# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DAddressType(models.Model):
    name = models.CharField(max_length=255)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'd_address_type'


class DIdcardType(models.Model):
    name = models.CharField(max_length=255)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'd_idcard_type'


class DPhoneType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'd_phone_type'


class DRegions(models.Model):
    name = models.CharField(max_length=255)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'd_regions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TAddresses(models.Model):
    address = models.CharField(max_length=500)
    id_person = models.ForeignKey('TPersons', models.DO_NOTHING, db_column='id_person')
    id_address_type = models.ForeignKey(DAddressType, models.DO_NOTHING, db_column='id_address_type')
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 't_addresses'


class TDebtData(models.Model):
    agr_num = models.CharField(max_length=255)
    issue_date = models.DateField()
    close_date = models.DateField()
    overdue_day = models.CharField(max_length=255)
    loan_amount = models.DecimalField(max_digits=80, decimal_places=3)
    claim_date = models.DateField()
    total_amount = models.DecimalField(max_digits=80, decimal_places=3)
    id_person = models.ForeignKey('TPersons', models.DO_NOTHING, db_column='id_person', blank=True, null=True)
    claim_amount = models.DecimalField(max_digits=80, decimal_places=3)
    main_debt = models.DecimalField(max_digits=80, decimal_places=3)
    percentage_debt = models.DecimalField(max_digits=80, decimal_places=3)
    fine_debt = models.DecimalField(max_digits=80, decimal_places=3)
    indebt_debt = models.DecimalField(max_digits=80, decimal_places=3)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 't_debt_data'


class TIdcard(models.Model):
    idcard_num = models.CharField(max_length=255)
    issue_date = models.DateField()
    given_by = models.CharField(max_length=255)
    id_person = models.ForeignKey('TPersons', models.DO_NOTHING, db_column='id_person')
    id_idcard_type = models.ForeignKey(DIdcardType, models.DO_NOTHING, db_column='id_idcard_type')
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 't_idcard'


class TPersons(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    iin = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=500)
    id_region = models.ForeignKey(DRegions, models.DO_NOTHING, db_column='id_region', blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    desc = models.TextField()
    id_rollback = models.DecimalField(max_digits=80, decimal_places=3)
    client_code = models.DecimalField(max_digits=80, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_persons'


class TPhones(models.Model):
    phone_num = models.CharField(max_length=255)
    id_person = models.ForeignKey(TPersons, models.DO_NOTHING, db_column='id_person')
    id_phone_type = models.ForeignKey(DPhoneType, models.DO_NOTHING, db_column='id_phone_type')
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 't_phones'


class TWork(models.Model):
    org_name = models.CharField(max_length=500)
    bin = models.DecimalField(max_digits=12, decimal_places=0)
    id_person = models.ForeignKey(TPersons, models.DO_NOTHING, db_column='id_person')

    class Meta:
        managed = False
        db_table = 't_work'
