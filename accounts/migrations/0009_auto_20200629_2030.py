# Generated by Django 2.2.9 on 2020-06-29 19:30

import accounts.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200629_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agent_Company', models.CharField(blank=True, max_length=1000, null=True)),
                ('Agent_Contact', models.CharField(blank=True, max_length=1000, null=True)),
                ('Fees_to_be_incurred_for_STS_Operations', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='headline',
        ),
        migrations.AddField(
            model_name='entry',
            name='agent_details',
            field=djongo.models.fields.EmbeddedModelField(model_container=accounts.models.Agent_Details, model_form_class=accounts.models.Agent_DetailsForm, null=True),
        ),
    ]
