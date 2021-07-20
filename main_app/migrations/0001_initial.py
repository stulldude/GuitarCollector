# Generated by Django 3.2.4 on 2021-07-19 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('gtrmodel', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod', models.CharField(max_length=100)),
                ('brand', models.CharField(default='stock', max_length=50)),
                ('mod_model', models.CharField(default='N/A', max_length=100)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.guitar')),
            ],
        ),
    ]