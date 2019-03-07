# Generated by Django 2.1.7 on 2019-03-06 03:27

import blog.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Album',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=50)),
        #         ('release_date', models.DateField()),
        #         ('num_stars', models.IntegerField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Comment',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('author', models.CharField(max_length=20)),
        #         ('message', models.CharField(max_length=100)),
        #         ('created_at', models.DateField(auto_now_add=True)),
        #         ('updated_at', models.DateTimeField(auto_now=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='FieldTest',
        #     fields=[
        #         ('fAutoField', models.AutoField(primary_key=True, serialize=False)),
        #         ('fBigIntegerField', models.BigIntegerField(default=1)),
        #         ('fBooleanField', models.BooleanField(default=True)),
        #         ('fCharField', models.CharField(default='엔코아', max_length=30)),
        #         ('fDateField', models.DateField(default=datetime.date.today)),
        #         ('fDateTimeField', models.DateTimeField()),
        #         ('fDecimalField', models.DecimalField(decimal_places=4, default=1.7321, max_digits=10)),
        #         ('fEmailField', models.EmailField(default='email@example.com', max_length=254)),
        #         ('fFloatField', models.FloatField(default=1.7321)),
        #         ('fIntegerField', models.IntegerField(default=10)),
        #         ('fGenericIPAddressField', models.GenericIPAddressField(default=None, unpack_ipv4=True)),
        #         ('fNullBooleanField', models.NullBooleanField(default=True)),
        #         ('fPositiveIntegerField', models.PositiveIntegerField(default=100)),
        #         ('fPositiveSmallIntegerField', models.PositiveSmallIntegerField(default=50)),
        #         ('fSlugField', models.SlugField(default='slug', max_length=30)),
        #         ('fSmallIntegerField', models.SmallIntegerField(default=-50)),
        #         ('fTextField', models.TextField(default='text text text text text text text')),
        #         ('fURLField', models.URLField(default='http://localhost')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Musician',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('first_name', models.CharField(max_length=50)),
        #         ('last_name', models.CharField(max_length=50)),
        #         ('instrument', models.CharField(max_length=50)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Person',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=255)),
        #         ('bio', models.CharField(blank=True, max_length=500)),
        #         ('bio2', models.CharField(max_length=500, null=True)),
        #         ('bio3', models.CharField(max_length=500, null=True)),
        #         ('birth_date', models.DateField()),
        #         ('contact_info', models.TextField(default=blog.models.Person.contact_default, verbose_name='연락처')),
        #         ('year_school', models.CharField(choices=[('FR', '1학년'), ('SO', '2학년'), ('JR', '3학년'), ('SR', '4학년')], default='FR', max_length=2)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Profile',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('phone', models.CharField(max_length=20)),
        #         ('address', models.CharField(max_length=40)),
        #         ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
        #     ],
        # ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title', '-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='even_field',
            field=models.IntegerField(default=0, validators=[blog.models.Post.validation_even]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='latlng',
            field=models.CharField(blank=True, help_text='위도와 경도를 입력하세요.', max_length=100, validators=[blog.models.Post.latlng_validation]),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='str_field',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='str_field2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
        # migrations.AddField(
        #     model_name='comment',
        #     name='post',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        # ),
        # migrations.AddField(
        #     model_name='album',
        #     name='artist',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Musician'),
        # ),
    ]