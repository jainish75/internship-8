# Generated by Django 4.0.2 on 2022-05-03 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_rename_m_menu_id_main_menu_mainmenu_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_menu',
            old_name='submen_id',
            new_name='submenu_id',
        ),
        migrations.RenameField(
            model_name='sub_menu',
            old_name='submen_link',
            new_name='submenu_link',
        ),
        migrations.RenameField(
            model_name='sub_menu',
            old_name='submen_name',
            new_name='submenu_name',
        ),
    ]
