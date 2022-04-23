# Generated by Django 2.2.24 on 2022-04-11 13:15

from django.db import migrations


def set_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owner_set = Owner.objects.all()
    if owner_set.exists():
        for owner in owner_set.iterator():
            flat, created = Flat.objects.get_or_create(owner=owner.name, owners_phonenumber=owner.owners_phonenumber)
            owner.flat.add(flat)
            flat.save()


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flat = ''
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220408_1302'),
    ]

    operations = [
        migrations.RunPython(set_flats_to_owners, move_backward),
    ]
