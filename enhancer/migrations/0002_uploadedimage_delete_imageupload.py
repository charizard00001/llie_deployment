# Generated by Django 5.1.4 on 2024-12-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enhancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_image', models.ImageField(upload_to='input_images/')),
                ('enhanced_image', models.ImageField(blank=True, null=True, upload_to='output_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageUpload',
        ),
    ]
