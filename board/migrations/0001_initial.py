# Generated by Django 3.0.8 on 2020-08-28 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ouruser', '0004_auto_20200716_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ouruser.Ouruser', verbose_name='작성자')),
            ],
            options={
                'db_table': 'django_board',
            },
        ),
    ]
