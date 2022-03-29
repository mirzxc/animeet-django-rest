# Generated by Django 4.0.3 on 2022-03-24 18:19

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_grade_unique_together_grade_unique_grade'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='grade',
            name='unique_grade',
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(django.db.models.expressions.F('user_id_given'), django.db.models.expressions.F('user_id_received'), name='unique_grade'),
        ),
    ]