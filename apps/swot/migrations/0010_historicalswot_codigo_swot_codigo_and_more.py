# Generated by Django 5.1.6 on 2025-02-09 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0009_alter_historicalswot_descricao_alter_swot_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalswot',
            name='codigo',
            field=models.CharField(db_comment='Codigo da avaliação SWOT', default='', editable=False, max_length=5),
        ),
        migrations.AddField(
            model_name='swot',
            name='codigo',
            field=models.CharField(db_comment='Codigo da avaliação SWOT', default='', editable=False, max_length=5),
        ),
        migrations.AddConstraint(
            model_name='swot',
            constraint=models.UniqueConstraint(fields=('codigo',), name='unique_codigo_swot'),
        ),
    ]
