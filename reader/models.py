from django.db import models
class SchoolClass(models.Model):
    numbers = models.CharField(max_length=3,primary_key=True,verbose_name='Номер класса')
    classroom_teacher = models.CharField(max_length=100,verbose_name='Классный руководитель')
    email_teacher = models.EmailField(verbose_name='Почта классного руководителя')
    def __str__(self):
        return self.numbers
    class Meta:
        verbose_name='Классы'
        verbose_name_plural='Классы'

class Reader(models.Model):

    CLASS_CHOICES=[('1А', '1А'), ('1Б', '1Б'), ('1В', '1В'), ('2А', '2А'), ('2Б', '2Б'), ('2В', '2В'), ('3А', '3А'), ('3Б', '3Б'), ('3В', '3В'), ('4А', '4А'), ('4Б', '4Б'), ('4В', '4В'), ('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('10А', '10А'), ('10Б', '10Б'), ('11А', '11А')]
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    full_name = models.CharField(max_length=100,verbose_name='Полное имя',default='-',null=True,blank=True)
    school_class = models.ForeignKey(SchoolClass,on_delete=models.PROTECT,verbose_name='Класс')

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'

        super(Reader,self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'
    def __str__(self):
        return f'{self.school_class}:{self.first_name} {self.last_name}'
# Create your models here.
