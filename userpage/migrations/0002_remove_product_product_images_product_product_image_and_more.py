# Generated by Django 5.0 on 2024-01-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_images',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='postmedia/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]