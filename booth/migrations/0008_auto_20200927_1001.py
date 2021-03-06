# Generated by Django 3.1.1 on 2020-09-27 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0007_auto_20200927_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='contractor_id',
            field=models.ForeignKey(db_column='contractor_id', on_delete=django.db.models.deletion.CASCADE, to='booth.contractor'),
        ),
        migrations.AlterField(
            model_name='booth',
            name='route_no',
            field=models.ForeignKey(db_column='route_no', on_delete=django.db.models.deletion.CASCADE, to='booth.route'),
        ),
        migrations.AlterField(
            model_name='itemmst',
            name='itemgroup_id',
            field=models.ForeignKey(db_column='itemgroup_id', on_delete=django.db.models.deletion.CASCADE, to='booth.itemgroup'),
        ),
        migrations.AlterField(
            model_name='route',
            name='contractor_id',
            field=models.ForeignKey(db_column='contractor_id', on_delete=django.db.models.deletion.CASCADE, to='booth.contractor'),
        ),
        migrations.AlterField(
            model_name='tran',
            name='booth_no',
            field=models.ForeignKey(db_column='booth_no', on_delete=django.db.models.deletion.CASCADE, to='booth.booth'),
        ),
        migrations.AlterField(
            model_name='tran',
            name='contractor_id',
            field=models.ForeignKey(db_column='contractor_id', on_delete=django.db.models.deletion.CASCADE, to='booth.contractor'),
        ),
        migrations.AlterField(
            model_name='tran',
            name='route_no',
            field=models.ForeignKey(db_column='route_no', on_delete=django.db.models.deletion.CASCADE, to='booth.route'),
        ),
        migrations.AlterField(
            model_name='trandet',
            name='booth_no',
            field=models.ForeignKey(db_column='booth_no', on_delete=django.db.models.deletion.CASCADE, to='booth.booth'),
        ),
        migrations.AlterField(
            model_name='trandet',
            name='item_id',
            field=models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='booth.itemmst'),
        ),
        migrations.AlterField(
            model_name='trandet',
            name='tran_id',
            field=models.ForeignKey(db_column='tran_id', on_delete=django.db.models.deletion.CASCADE, to='booth.tran'),
        ),
    ]
