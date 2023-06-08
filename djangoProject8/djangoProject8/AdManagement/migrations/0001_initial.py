# Generated by Django 4.0.6 on 2022-07-26 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Img', models.ImageField(upload_to='')),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('V_date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdManagement.ad')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdManagement.ad')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='Adv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdManagement.advertiser'),
        ),
    ]