# Generated by Django 3.1.7 on 2021-02-23 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TechShelterApp', '0002_auto_20210221_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techname', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
