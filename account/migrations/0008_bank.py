# Generated by Django 2.2 on 2019-10-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_merchantpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=100)),
                ('account_no', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=20)),
            ],
        ),
    ]
