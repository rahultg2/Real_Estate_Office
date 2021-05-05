# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_no = models.IntegerField(db_column='Address_NO', primary_key=True)  # Field name made lowercase.
    locality = models.CharField(db_column='Locality', max_length=60, blank=True, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='PinCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'address'


class Agent(models.Model):
    agent_id = models.IntegerField(db_column='Agent_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=15, blank=True, null=True)  # Field name made lowercase.
    number_of_properties_sold = models.IntegerField(db_column='Number_of_Properties_Sold', blank=True, null=True)  # Field name made lowercase.
    number_of_properties_rented = models.IntegerField(db_column='Number_of_Properties_Rented', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'agent'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Estate(models.Model):
    serial_no = models.IntegerField(db_column='Serial_No', primary_key=True)  # Field name made lowercase.
    agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent_ID', blank=True, null=True)  # Field name made lowercase.
    address_no = models.ForeignKey(Address, models.DO_NOTHING, db_column='Address_No', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_Id', blank=True, null=True)  # Field name made lowercase.
    available_for = models.CharField(db_column='Available_For', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    selling_price = models.IntegerField(db_column='Selling_Price', blank=True, null=True)  # Field name made lowercase.
    bhk = models.IntegerField(db_column='BHK', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    plot_area = models.IntegerField(db_column='Plot_Area', blank=True, null=True)  # Field name made lowercase.
    parking_available = models.CharField(db_column='Parking_Available', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_of_sale_or_rent = models.CharField(db_column='Date_of_Sale_OR_Rent', max_length=30, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'estate'


class Users(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'users'
