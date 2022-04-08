# Generated by Django 2.2.24 on 2022-04-07 12:50

from django.db import migrations
import phonenumbers


def pure_owners_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
            flat.owner_pure_phone = phonenumbers.format_number(
                parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220407_1240'),
    ]

    operations = [
        migrations.RunPython(pure_owners_phonenumber, move_backward),
    ]
