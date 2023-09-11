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
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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

class Users(models.Model):
    username = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    profileimg = models.CharField(max_length=255)
    actoractorfollowers = models.CharField(max_length=255)
    subscriptions = models.CharField(max_length=255)
    sociallinks = models.CharField(max_length=255)
    contents = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'users'

class Tags(models.Model):
    name = models.CharField(max_length=255)
    categoryname = models.CharField(max_length=255)
    class Meta:
        managed=True
        db_table='tags'

class Influence(models.Model):
    name = models.CharField(max_length=255)
    subscriber = models.CharField(max_length=255)
    views = models.CharField(max_length=255)
    cpm = models.CharField(max_length=255)
    likes = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    operating = models.CharField(max_length=255)
    class Meta:
        managed=True
        db_table='influence'

class Contents(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    somenameurl = models.CharField(max_length=255)
    upload = models.CharField(max_length=255)
    playtime = models.CharField(max_length=255)
    crawling = models.CharField(max_length=255)
    likes = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    views = models.CharField(max_length=255)
    shares = models.CharField(max_length=255)
    saVES = models.CharField(max_length=255)
    subscriber = models.CharField(max_length=255)
    relatedvideos = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    class Meta:
        managed=True
        db_table='contents'
class Front(models.Model):
    categories = models.CharField(max_length=255)
    channelMood = models.CharField(max_length=255)
    channelPurpose = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    interests = models.CharField(max_length=255)
    mbti = models.CharField(max_length=255)
    videoStyle = models.CharField(max_length=255)

    class Meta:
        managed=True
        db_table='front'