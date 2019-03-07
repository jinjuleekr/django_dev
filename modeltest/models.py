from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        #return "{} {}".format(self.last_name, self.first_name)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-title",)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) #1:n
    publication = models.ManyToManyField(Publication) #n:m의 관계라서 중간테이블이 생성됨 따라서 CASECADE를 설정할 수 없음

    def __str__(self):
        return self.headline

    class Meta: #사용자에게 보여주기 위한 화면 // ordering은 예약어
        ordering = ('headline',)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address =models.CharField(max_length=50)

    def __str__(self):
        return "{}로 오시면 됩니다.".format(self.name)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    service_hot_dogs = models.BooleanField(default=False)
    service_pizza = models.BooleanField(default=False)

    def __str__(self):
        return '{}식당의 장소는 {} 입니다.'.format(self.place.name, self.place.address)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, 스텝은 {}입니다.".format(self.restaurant, self.name)