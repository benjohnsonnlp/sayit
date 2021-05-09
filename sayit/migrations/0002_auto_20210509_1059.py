# Generated by Django 3.0.5 on 2021-05-09 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField()),
                ('artist', models.TextField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayit.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sayit.Session'),
        ),
    ]
