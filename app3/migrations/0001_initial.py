# Generated by Django 4.0.2 on 2022-05-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/detail')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='main_menu',
            fields=[
                ('m_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_menu_name', models.CharField(max_length=50)),
                ('m_menu_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='sub_menu',
            fields=[
                ('s_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_menu_id', models.IntegerField()),
                ('s_menu_name', models.CharField(max_length=50)),
                ('s_menu_link', models.CharField(max_length=100)),
            ],
        ),
    ]