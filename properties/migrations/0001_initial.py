# Generated by Django 3.1.6 on 2021-03-16 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_secret_key', models.CharField(max_length=225)),
                ('text_public_key', models.CharField(max_length=225)),
                ('live_public_key', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=35)),
                ('location', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30, null=True)),
                ('property_lease', models.CharField(max_length=100)),
                ('lease_options', models.CharField(max_length=50, null=True)),
                ('property_type', models.CharField(choices=[('1', 'Apartment'), ('2', 'Land'), ('3', 'Full House'), ('3', 'Office Space')], max_length=15)),
                ('duration', models.IntegerField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('owner', models.CharField(max_length=30, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='properties/listings/')),
                ('has_balcony', models.BooleanField(default=False)),
                ('price_negotiable', models.BooleanField(default=False)),
                ('fully_furnished', models.BooleanField(default=False)),
                ('no_of_rooms', models.IntegerField(verbose_name=10)),
                ('no_of_baths', models.IntegerField(verbose_name=10)),
                ('full_property_description', models.TextField()),
                ('floor_area', models.IntegerField(blank=True)),
                ('dimensions', models.CharField(max_length=30)),
                ('reference', models.CharField(blank=True, max_length=35, null=True)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_Id', models.CharField(max_length=50)),
                ('prop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
        ),
    ]
