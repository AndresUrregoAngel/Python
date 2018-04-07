# Generated by Django 2.0.3 on 2018-03-31 23:22

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
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_desc', models.CharField(max_length=500)),
                ('correct', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PortalUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='subject_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject_category'),
        ),
        migrations.AddField(
            model_name='answer',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject_category'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.questions'),
        ),
        migrations.AddField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject'),
        ),
    ]