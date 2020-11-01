# Generated by Django 2.2.4 on 2019-08-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_redirect", "0002_auto_20170321_1807"),
    ]

    operations = [
        migrations.AddField(
            model_name="redirect",
            name="catchall_redirect",
            field=models.BooleanField(
                default=False,
                help_text="If selected all the pages starting with the given string will be redirected to the given redirect path",
                verbose_name="Catchall redirect",
            ),
        ),
        migrations.AddField(
            model_name="redirect",
            name="subpath_match",
            field=models.BooleanField(
                default=False,
                help_text="If selected all the pages starting with the given string will be redirected by replacing the matching subpath with the provided redirect path.",
                verbose_name="Subpath match",
            ),
        ),
    ]
