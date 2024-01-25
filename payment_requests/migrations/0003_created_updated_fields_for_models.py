# Generated by Django 5.0.1 on 2024-01-25 20:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_requests', '0002_default_values_for_CheckingAccount_and_indexing_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkingaccount',
            options={'ordering': ['-created_at'], 'verbose_name': 'Реквизит', 'verbose_name_plural': 'Реквизиты'},
        ),
        migrations.AlterModelOptions(
            name='paymentrequest',
            options={'ordering': ['-created_at'], 'verbose_name': 'Заявка на оплату', 'verbose_name_plural': 'Заявки на оплату'},
        ),
        migrations.AddField(
            model_name='checkingaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkingaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата и время обновления'),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата и время обновления'),
        ),
    ]
