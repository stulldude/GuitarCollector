# Generated by Django 3.2.4 on 2021-07-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('amp_model', models.CharField(max_length=50)),
                ('style', models.CharField(choices=[('C', 'Combo'), ('S', 'Stack')], default='C', max_length=1, verbose_name='Stack or Combo')),
            ],
        ),
        migrations.AddField(
            model_name='guitar',
            name='amps',
            field=models.ManyToManyField(to='main_app.Amp'),
        ),
    ]
