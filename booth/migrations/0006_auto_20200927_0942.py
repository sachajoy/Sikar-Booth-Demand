# Generated by Django 3.1.1 on 2020-09-27 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0005_shift_tran_trandet'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booth',
            table='booth',
        ),
        migrations.AlterModelTable(
            name='contractor',
            table='contractor',
        ),
        migrations.AlterModelTable(
            name='itemgroup',
            table='itemgroup',
        ),
        migrations.AlterModelTable(
            name='itemmst',
            table='itemmst',
        ),
        migrations.AlterModelTable(
            name='route',
            table='route',
        ),
        migrations.AlterModelTable(
            name='shift',
            table='shift',
        ),
        migrations.AlterModelTable(
            name='tran',
            table='tran',
        ),
    ]
