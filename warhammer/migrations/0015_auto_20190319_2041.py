# Generated by Django 2.1.4 on 2019-03-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warhammer', '0014_auto_20190318_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterabilities',
            name='stat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warhammer.StatsModel'),
        ),
        migrations.AlterField(
            model_name='characterabilities',
            name='stat_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterskills',
            name='bonus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
