# Generated by Django 4.1.2 on 2022-10-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretarias', '0003_alter_secretaria_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalsecretaria',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical secretaria', 'verbose_name_plural': 'historical secretarias'},
        ),
        migrations.AlterField(
            model_name='historicalsecretaria',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
