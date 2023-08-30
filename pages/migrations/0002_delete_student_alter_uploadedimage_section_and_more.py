# Generated by Django 4.1.7 on 2023-08-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='specialization',
            field=models.CharField(choices=[('CSE', 'CSE'), ('AIML', 'AIML'), ('BDA', 'BDA'), ('CSBS', 'CSBS')], max_length=4),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='year',
            field=models.IntegerField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')]),
        ),
    ]
