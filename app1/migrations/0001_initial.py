# Generated by Django 4.2.2 on 2023-06-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcid', models.IntegerField()),
                ('pcname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
                ('pdesc', models.TextField()),
                ('pdate', models.DateField()),
                ('pcname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product_category')),
            ],
        ),
    ]
