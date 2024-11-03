# Generated by Django 5.1.2 on 2024-11-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_course_lecturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submission_file_path',
        ),
        migrations.AddField(
            model_name='submission',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='graded_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Graded', 'Graded')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='submission',
            name='submission_file',
            field=models.FileField(default=1, upload_to='submissions/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='lecturer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submission',
            name='student',
            field=models.CharField(max_length=100),
        ),
    ]