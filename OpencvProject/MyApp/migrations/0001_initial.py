# Generated by Django 4.1 on 2022-08-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='Activities/')),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Criminals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('residence', models.CharField(max_length=50)),
                ('country', models.CharField(default='Tanzania', max_length=50)),
                ('education', models.CharField(blank=True, max_length=150, null=True)),
                ('occupation', models.CharField(blank=True, max_length=150, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(choices=[('', 'Choose Gender'), ('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to='crimanls/')),
            ],
            options={
                'verbose_name_plural': 'Criminals',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_name', models.CharField(blank=True, max_length=200, null=True)),
                ('case_records', models.TextField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('criminals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.criminals')),
            ],
        ),
    ]
