# Generated by Django 2.0.6 on 2018-10-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Catch', '0003_auto_20181006_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=40)),
                ('team_level', models.CharField(choices=[('U09', 'Under 09s'), ('U10', 'Under 10s'), ('U11', 'Under 11s')], default='U11', max_length=3)),
            ],
        ),
    ]