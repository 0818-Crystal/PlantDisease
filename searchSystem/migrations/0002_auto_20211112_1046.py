# Generated by Django 3.2.8 on 2021-11-12 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searchSystem', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500, null=True)),
                ('is_answered', models.BooleanField()),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True, null=True)),
                ('answer_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_from+', to=settings.AUTH_USER_MODEL)),
                ('question_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_from+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
