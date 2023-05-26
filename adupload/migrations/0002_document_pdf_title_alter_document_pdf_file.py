# Generated by Django 4.2.1 on 2023-05-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='pdf_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='pdf_file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='documents/'),
        ),
    ]