
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_nom = models.CharField(db_column='CLI_NOM', max_length=50)  # Field name made lowercase.
    cli_prenom = models.CharField(db_column='CLI_PRENOM', max_length=50)  # Field name made lowercase.
    cli_mail = models.CharField(db_column='CLI_MAIL', max_length=50)  # Field name made lowercase.
    cli_adresse = models.CharField(db_column='CLI_ADRESSE', max_length=250)  # Field name made lowercase.
    cli_codepos = models.IntegerField(db_column='CLI_CODEPOS')  # Field name made lowercase.
    cli_ville = models.CharField(db_column='CLI_VILLE', max_length=50)  # Field name made lowercase.
    cli_telephone = models.CharField(db_column='CLI_TELEPHONE', max_length=10)  # Field name made lowercase.
    cli_club = models.CharField(db_column='CLI_CLUB', max_length=50)  # Field name made lowercase.
    cli_club_ville = models.CharField(db_column='CLI_CLUB_VILLE', max_length=50)  # Field name made lowercase.
    pos = models.ForeignKey('Postes', models.DO_NOTHING, db_column='POS_ID', blank=True, null=True)  # Field name made lowercase.
    sec = models.ForeignKey('Section', models.DO_NOTHING, db_column='SEC_ID', blank=True, null=True)  # Field name made lowercase.
    division = models.ForeignKey('Division', models.DO_NOTHING, db_column='DIVISION_ID', blank=True, null=True)  # Field name made lowercase.
    pied = models.ForeignKey('Pied', models.DO_NOTHING, db_column='PIED_ID', blank=True, null=True)  # Field name made lowercase.
    typ = models.ForeignKey('TypeCli', models.DO_NOTHING, db_column='TYP_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Concerne(models.Model):
    suivobs = models.ForeignKey('Suivobs', models.DO_NOTHING, db_column='SUIVOBS_ID', primary_key=True)  # Field name made lowercase.
    cli = models.ForeignKey(Client, models.DO_NOTHING, db_column='CLI_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'concerne'
        unique_together = (('suivobs', 'cli'),)


class Division(models.Model):
    division_id = models.AutoField(db_column='DIVISION_ID', primary_key=True)  # Field name made lowercase.
    division_nom = models.CharField(db_column='DIVISION_NOM', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'division'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class PagesPage(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(unique=True, max_length=12)
    bodytext = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_page'


class Pied(models.Model):
    pied_id = models.AutoField(db_column='PIED_ID', primary_key=True)  # Field name made lowercase.
    pied_nom = models.CharField(db_column='PIED_NOM', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pied'


class Postes(models.Model):
    pos_id = models.AutoField(db_column='POS_ID', primary_key=True)  # Field name made lowercase.
    pos_nom = models.CharField(db_column='POS_NOM', max_length=50)  # Field name made lowercase.
    pos_type = models.CharField(db_column='POS_TYPE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postes'


class Section(models.Model):
    sec_id = models.AutoField(db_column='SEC_ID', primary_key=True)  # Field name made lowercase.
    sec_nom = models.CharField(db_column='SEC_NOM', max_length=5)  # Field name made lowercase.
    sec_age_max = models.IntegerField(db_column='SEC_AGE_MAX')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'section'


class Suivobs(models.Model):
    suivobs_id = models.AutoField(db_column='SUIVOBS_ID', primary_key=True)  # Field name made lowercase.
    suivobs_date = models.DateField(db_column='SUIVOBS_DATE')  # Field name made lowercase.
    suivobs_theme = models.CharField(db_column='SUIVOBS_THEME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suivobs_travail = models.TextField(db_column='SUIVOBS_TRAVAIL', blank=True, null=True)  # Field name made lowercase.
    suivobs_observation = models.TextField(db_column='SUIVOBS_OBSERVATION')  # Field name made lowercase.
    suivobs_axeprogres = models.TextField(db_column='SUIVOBS_AXEPROGRES')  # Field name made lowercase.
    suivobs_video = models.CharField(db_column='SUIVOBS_VIDEO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suivobs_resultat = models.CharField(db_column='SUIVOBS_RESULTAT', max_length=25, blank=True, null=True)  # Field name made lowercase.
    suivobs_but = models.IntegerField(db_column='SUIVOBS_BUT', blank=True, null=True)  # Field name made lowercase.
    suivobs_passe = models.IntegerField(db_column='SUIVOBS_PASSE', blank=True, null=True)  # Field name made lowercase.
    typsuivi = models.ForeignKey('Typsuivi', models.DO_NOTHING, db_column='TYPSUIVI_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suivobs'


class TypeCli(models.Model):
    typ_id = models.AutoField(db_column='TYP_ID', primary_key=True)  # Field name made lowercase.
    typ_nom = models.CharField(db_column='TYP_NOM', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type_cli'


class Typsuivi(models.Model):
    typsuivi_id = models.AutoField(db_column='TYPSUIVI_ID', primary_key=True)  # Field name made lowercase.
    typsuivi_nom = models.CharField(db_column='TYPSUIVI_NOM', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typsuivi'