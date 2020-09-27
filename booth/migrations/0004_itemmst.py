# Generated by Django 3.1.1 on 2020-09-27 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0003_itemgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xname', models.CharField(default='', max_length=32)),
                ('shortname', models.CharField(default='', max_length=8)),
                ('itype', models.CharField(default='', max_length=1)),
                ('unit', models.CharField(default='', max_length=8)),
                ('packingtype', models.CharField(default='', max_length=8)),
                ('sale_unit', models.CharField(default='', max_length=8)),
                ('qty_fill', models.DecimalField(decimal_places=3, max_digits=15)),
                ('active', models.BooleanField(default=True)),
                ('itemgroup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.itemgroup')),
            ],
        ),
    ]