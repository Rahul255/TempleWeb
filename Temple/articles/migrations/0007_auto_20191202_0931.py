# Generated by Django 2.2.6 on 2019-12-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20191126_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='god',
            field=models.CharField(choices=[('Krishna', 'Krishna'), ('Ganapathi', 'Ganapathi'), ('Devi', 'Devi'), ('Ayyappa', 'Ayyappa')], max_length=255, verbose_name='God'),
        ),
    ]
