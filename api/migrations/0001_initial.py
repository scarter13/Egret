# Generated by Django 3.0.7 on 2020-07-02 00:55

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
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(choices=[('C_ONE', 'Color 1'), ('C_TWO', 'Color 2'), ('C_THREE', 'Color 3'), ('C_FOUR', 'Color 4'), ('C_FIVE', 'Color 5'), ('C_SIX', 'Color 6'), ('C_SEVEN', 'Color 7'), ('C_EIGHT', 'Color 8')], default='C_ONE', max_length=25)),
                ('font', models.CharField(choices=[('F_ONE', 'Font 1'), ('F_TWO', 'Font 2'), ('F_THREE', 'Font 3'), ('F_FOUR', 'Font 4'), ('F_FIVE', 'Font 5'), ('F_SIX', 'Font 6'), ('F_SEVEN', 'Font 7'), ('F_EIGHT', 'Font 8')], default='F_ONE', max_length=25)),
                ('outer_text', models.TextField(blank=True, null=True)),
                ('inner_text', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
