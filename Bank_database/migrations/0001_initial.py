# Generated by Django 4.1.7 on 2023-08-05 14:56

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
            name='Kerelem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osszeg', models.FloatField()),
                ('futamido', models.IntegerField()),
                ('kamat', models.FloatField()),
                ('felvett', models.BooleanField()),
                ('leiras', models.TextField()),
                ('torlesztett', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Szamla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aktualis_osszeg', models.FloatField()),
                ('szamla_tipus', models.TextField(max_length=255)),
                ('szamla_tulajdonos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tranzakcio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField()),
                ('osszeg', models.FloatField()),
                ('tranzakcio_fajta', models.CharField(max_length=255)),
                ('szamla_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.szamla')),
            ],
        ),
        migrations.CreateModel(
            name='Torlesztes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osszeg', models.FloatField()),
                ('kerelem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.kerelem')),
                ('szamla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.szamla')),
            ],
        ),
        migrations.AddField(
            model_name='kerelem',
            name='szamla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.szamla'),
        ),
        migrations.CreateModel(
            name='Befektetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osszeg', models.FloatField()),
                ('torlesztett', models.FloatField()),
                ('kerelem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.kerelem')),
                ('szamla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank_database.szamla')),
            ],
        ),
    ]
