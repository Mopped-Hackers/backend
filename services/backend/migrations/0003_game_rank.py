# Generated by Django 4.0.4 on 2022-04-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_game_bought_game_viewed_alter_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rank',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]