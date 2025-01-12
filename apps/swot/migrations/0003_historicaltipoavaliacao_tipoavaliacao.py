# Generated by Django 5.1.4 on 2025-01-12 02:40

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0002_alter_historicaltipoambiente_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTipoAvaliacao',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('data_inclusao', models.DateField(blank=True, editable=False, verbose_name='Data de Inclusão')),
                ('hora_inclusao', models.DateTimeField(blank=True, editable=False, verbose_name='Hora de Inclusão')),
                ('data_alteracao', models.DateField(blank=True, editable=False, verbose_name='Data de Alteração')),
                ('hora_alteracao', models.DateTimeField(blank=True, editable=False, verbose_name='Hora de Alteração')),
                ('nome', models.CharField(db_comment='Nome do tipo de avaliação', db_index=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tipo_ambiente', models.ForeignKey(blank=True, db_comment='Tipo de ambiente relacionado', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='swot.tipoambiente')),
            ],
            options={
                'verbose_name': 'historical Tipo de Avaliação',
                'verbose_name_plural': 'historical Tipos de Avaliação',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='TipoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inclusao', models.DateField(auto_now_add=True, verbose_name='Data de Inclusão')),
                ('hora_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Inclusão')),
                ('data_alteracao', models.DateField(auto_now=True, verbose_name='Data de Alteração')),
                ('hora_alteracao', models.DateTimeField(auto_now=True, verbose_name='Hora de Alteração')),
                ('nome', models.CharField(db_comment='Nome do tipo de avaliação', max_length=100, unique=True)),
                ('tipo_ambiente', models.ForeignKey(db_comment='Tipo de ambiente relacionado', on_delete=django.db.models.deletion.PROTECT, to='swot.tipoambiente')),
            ],
            options={
                'verbose_name': 'Tipo de Avaliação',
                'verbose_name_plural': 'Tipos de Avaliação',
                'db_table_comment': 'Tipo de Avaliação da análise SWOT',
            },
        ),
    ]
