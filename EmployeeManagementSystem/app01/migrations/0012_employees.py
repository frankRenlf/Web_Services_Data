# Generated by Django 4.1.7 on 2023-03-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
