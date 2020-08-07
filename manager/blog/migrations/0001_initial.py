# Generated by Django 3.0.9 on 2020-08-07 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('slug', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='users.Users')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]