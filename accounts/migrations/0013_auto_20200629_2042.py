# Generated by Django 2.2.9 on 2020-06-29 19:42

import accounts.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200629_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tug_Provider_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tug_Provider_Company', models.CharField(blank=True, max_length=1000, null=True)),
                ('Tug_Provider_Contact', models.CharField(blank=True, max_length=1000, null=True)),
                ('Tug_Provider_Vessel_Name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tug_provider_details',
            field=djongo.models.fields.EmbeddedModelField(model_container=accounts.models.Tug_Provider_Details, model_form_class=accounts.models.Tug_Provider_DetailsForm, null=True),
        ),
    ]
