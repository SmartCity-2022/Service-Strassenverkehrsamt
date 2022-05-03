# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bill(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    value = models.FloatField()
    description = models.CharField(max_length=100)
    issued = models.DateTimeField()
    payed = models.DateTimeField(blank=True, null=True)
    receiver = models.IntegerField()
    deadline = models.DateTimeField()
    on_delete = models.on

    class Meta:
        managed = False
        db_table = 'bill'


class License(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    owner = models.IntegerField()
    type = models.CharField(max_length=10)
    received = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'license'


class Licenserequest(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    citizen = models.IntegerField()
    form = models.CharField(max_length=500)
    issued = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'licenserequest'


class Penalty(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    owner = models.IntegerField()
    received = models.DateTimeField()
    value = models.IntegerField()
    reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'penalty'


class Registerrequest(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    registration1 = models.CharField(max_length=500)
    registration2 = models.CharField(max_length=500)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicle')
    hucertificate = models.CharField(db_column='huCertificate', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registerrequest'


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=true, auto_created=true)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    firstregistration = models.DateTimeField(db_column='firstRegistration')  # Field name made lowercase.
    displacement = models.FloatField()
    fueltype = models.CharField(db_column='fuelType', max_length=45)  # Field name made lowercase.
    emissions = models.FloatField()
    hudeadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'
