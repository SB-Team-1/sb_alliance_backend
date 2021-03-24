# Generated by Django 3.0 on 2021-03-24 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('1', 'Electronics'), ('2', 'Auto'), ('3', 'Food/Beverage'), ('4', 'Health/Fitness'), ('5', 'Apparel'), ('6', 'Furniture'), ('7', 'Sporting goods'), ('8', 'Home Improvement'), ('9', 'Misc')], max_length=1)),
                ('description', models.TextField(max_length=750)),
                ('website', models.URLField()),
                ('favorite', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discounts', models.TextField(max_length=750)),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perks', to='api.Alliance')),
            ],
        ),
        migrations.AddField(
            model_name='alliance',
            name='business',
            field=models.ManyToManyField(to='api.Business'),
        ),
        migrations.AddField(
            model_name='alliance',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]