# Generated by Django 2.2.3 on 2019-07-18 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_open', models.DateField(blank=True, null=True)),
                ('date_of_close', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('is_cash', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Account')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'db_table': 'income',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('cash_back', models.FloatField(default=0.0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Account')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]
