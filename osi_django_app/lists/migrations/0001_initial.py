# Generated by Django 2.2.1 on 2019-05-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('stripend', models.BooleanField(default=False)),
                ('timeline', models.URLField()),
            ],
        ),
    ]
