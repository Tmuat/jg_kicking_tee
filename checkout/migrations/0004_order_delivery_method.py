# Generated by Django 3.1.7 on 2021-03-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210312_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_option', to='checkout.deliveryoptions'),
            preserve_default=False,
        ),
    ]