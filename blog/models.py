from django.db import models
from django.core.exceptions import ValidationError
import re
import datetime
import json
from django.contrib.auth.models import User
from django.conf import settings

# class 1개가 테이블 1개가 됨
class Post(models.Model):
    name = models.TextField()
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post_set')

    def latlng_validation(value):
        check = re.match(r'(\d+\.?\d*),(\d+\.?\d*)', value) #위도, 경도 표시
        if not check:
            raise ValidationError("유효하지 않은 위도, 경도입니다.")
    latlng = models.CharField(max_length=100, blank=True,
                validators=[latlng_validation],
                help_text="위도와 경도를 입력하세요.")

    def validation_even(value):
        if value%2!=0:
            raise ValidationError(str(value) + "는 짝수여야합니다.")

    even_field = models.IntegerField(validators=[validation_even])
    str_field = models.CharField(max_length=50)
    str_field2 = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.title + "-" + str(self.id)
 
    class Meta: #sort를 간편하게 하는 방법
        ordering = ['title','-id'] #id로 ascending

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name + self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

class FieldTest(models.Model):
    fAutoField = models.AutoField(primary_key=True)
    fBigIntegerField = models.BigIntegerField(default=1)
    fBooleanField = models.BooleanField(default=True)
    fCharField = models.CharField(default='엔코아', max_length=30)
    fDateField = models.DateField(auto_now=False, default=datetime.date.today)

    # auto_now = False: 현재일자로 저장시마다 수정
    # auto_now = True: 현재일자로 저장시마다 수정 불가
    # auto_now_add = True: 현재일자로 최초 1회만 들어감
    # auto_now_add = false: 선택일자로 최초 1회만 들어감

    fDateTimeField = models.DateTimeField(auto_now=False, auto_now_add=False)
    fDecimalField = models.DecimalField(default=1.7321, decimal_places=4, max_digits=10)
    fEmailField = models.EmailField(default="email@example.com")
    fFloatField = models.FloatField(default=1.7321)
    fIntegerField = models.IntegerField(default=10)
    fGenericIPAddressField = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, default=None)
    fNullBooleanField = models.NullBooleanField(default=True)
    fPositiveIntegerField = models.PositiveIntegerField(default=100)
    fPositiveSmallIntegerField = models.PositiveSmallIntegerField(default=50)
    fSlugField = models.SlugField(max_length=30, default='slug')
    fSmallIntegerField = models.SmallIntegerField(default=-50)
    fTextField = models.TextField(default="text text text text text text text")
    fURLField = models.URLField(max_length=200, default='http://localhost')


class Person(models.Model):
    name = models.CharField(max_length=255) #blank = False null=False
    bio = models.CharField(max_length=500, blank=True) #null = False ==> (빈문자 : '')
    bio2 = models.CharField(max_length=500, null=True) #blank = False ==> 논리 에러(필수 칼럼)
    bio3 = models.CharField(max_length=500, null=True) #blank = True null=True
    #오늘날짜가 입력되고, 수정 가능함
    birth_date = models.DateField(auto_now = False) 

    def contact_default():
        return {"email":"jinju@gmail.com"}

    contact_info = models.TextField("연락처", default = contact_default)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICE = (
        (FRESHMAN, '1학년'),
        (SOPHOMORE, '2학년'),
        (JUNIOR, '3학년'),
        (SENIOR, '4학년')
    )
    year_school= models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICE, default = FRESHMAN)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.user

