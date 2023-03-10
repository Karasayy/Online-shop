# Generated by Django 3.2 on 2023-01-30 20:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onshop', '0002_auto_20230131_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Опубликовано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='onshop.rubric', verbose_name='Рубрика'),
        ),
    ]
