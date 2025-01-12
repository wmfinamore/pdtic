# Generated by Django 5.1.4 on 2025-01-12 03:06

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0006_historicalswot_swot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalswot',
            name='tipo_avaliacao',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='tipo_ambiente', chained_model_field='tipo_ambiente', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', show_all=True, to='swot.tipoavaliacao'),
        ),
        migrations.AlterField(
            model_name='swot',
            name='tipo_avaliacao',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='tipo_ambiente', chained_model_field='tipo_ambiente', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='swot.tipoavaliacao'),
        ),
    ]
