# Generated by Django 4.2.5 on 2023-11-26 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='TransactionItem',
        ),
        migrations.AlterModelTable(
            name='transactionitem',
            table='TransactionItem',
        ),
    ]