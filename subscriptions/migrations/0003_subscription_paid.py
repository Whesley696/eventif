# Generated by Django 4.2.1 on 2023-10-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "subscriptions",
            "0002_alter_subscription_options_alter_subscription_cpf_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="paid",
            field=models.BooleanField(default=False, verbose_name="pago"),
        ),
    ]
