# Generated by Django 3.1 on 2020-08-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200812_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='text'),
        ),
    ]
