# Generated by Django 2.2.6 on 2019-10-01 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('cp', models.CharField(max_length=10)),
                ('local', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_type', models.CharField(max_length=20)),
                ('value', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('website', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eurocv.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_type', models.CharField(max_length=15)),
                ('country_prefix', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_type', models.CharField(max_length=15)),
                ('country_prefix', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=40)),
                ('stat_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eurocv.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('nationality', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=15)),
                ('photo', models.TextField()),
                ('desired_job', models.CharField(max_length=100)),
                ('business_sector', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eurocv.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=15)),
                ('work_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eurocv.WorkExperience')),
            ],
        ),
    ]
