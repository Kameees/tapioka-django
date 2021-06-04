# Generated by Django 3.2.4 on 2021-06-04 06:52

from django.db import migrations, models
import django.db.models.deletion
import gallery.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', gallery.fields.ThumbnailImageField(upload_to='photos')),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]