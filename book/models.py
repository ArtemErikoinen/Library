from django.db import models

# Create your models here.
from django.db import models
import qrcode
from django.db import models
import qrcode
from reader.models import *
from django.contrib.auth.models import User
from django.db.models import Value
from django.db.models import F

from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile

from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files import File
from reader.models import Reader
import datetime
from django.db.models import Q



class Book(models.Model):
    @classmethod
    def make_qr_code(cls):
        pass




    YEAR_CHOICES = [(1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)]
    name=models.CharField(max_length=256,verbose_name='Название')
    year=models.IntegerField(choices=YEAR_CHOICES,verbose_name='Год')
    author=models.CharField(max_length=120,verbose_name='Автор')
    publishing_house=models.CharField(max_length=120,verbose_name='Издательство')
    numbers=models.IntegerField(verbose_name='ИН')
    menu_qr_code = models.ImageField(upload_to='img/qr_code/',blank=True,verbose_name='QR-CODE',unique=True,default=None)



    def save(self, *args, **kwargs):
        img = qrcode.make(f'http://192.168.31.186:8000/admin/book/book/{self.id}/change/')
        font1 = ImageFont.truetype('C:/Users/Артем/Library/ttf/Nunito.ttf', size=24)
        font2 = ImageFont.truetype('C:/Users/Артем/Library/ttf/Nunito.ttf', size=16)
        canvas = Image.new('RGBA',[1000,400],(255, 0, 0, 0),)
        canvas.paste(img)  # Error occurs on this line
        draw = ImageDraw.Draw(canvas)
        draw.text(
            (420, 50),
            f'Автор: {self.author}',
            font=font1,
            fill=('#1C0606'),

        )
        draw.text(
            (420, 110),
            f'Название: {self.name}',
            font=font2,
            fill=('#1C0606'),

        )
        draw.text(
            (420, 170),
            f'Год: {self.year}',
            font=font1,
            fill=('#1C0606'),

        )
        draw.text(
            (420, 230),
            f'Издательство: {self.publishing_house}',
            font=font1,
            fill=('#1C0606'),
        )
        draw.text(
            (420, 290),
            f'ИН: {self.numbers}',
            font=font1,
            fill=('#1C0606'),
        )


        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        canvas.close()
        fname = f'qr-code-{self.name}.png'
        self.menu_qr_code.save(fname, File(buffer),save=False)

        super(Book,self).save(*args, **kwargs)


    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'Художественная литература'
        verbose_name_plural = 'Художественная литература'

class HistoryBook(models.Model):



    book = models.ForeignKey(Book, on_delete=models.CASCADE,default=1,verbose_name='Книга')



    name=models.ForeignKey(Reader,on_delete=models.PROTECT,verbose_name='ФИ',related_name='book_id')


    data_of_capture=models.CharField(default=datetime.date.today() ,verbose_name='Дата выдачи',max_length=20)
    data_of_return = models.CharField(verbose_name='Дата возврата',max_length=20,blank=True,null=True)
    extradition = models.BooleanField(verbose_name='Выдача',default=True)
    def save(self, *args, **kwargs):
        if self.extradition==True:
            self.data_of_return='-'
        else:
            self.data_of_return = datetime.date.today()


        super(HistoryBook,self).save(*args, **kwargs)


    def __str__(self):
        return f'Выдача'


    class Meta:
        verbose_name = 'Формуляр'
        verbose_name_plural = 'Формуляр'