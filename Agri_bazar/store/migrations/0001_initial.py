# Generated by Django 3.1.3 on 2020-12-06 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField(default=0)),
                ('weight', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='photos/product/%y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
