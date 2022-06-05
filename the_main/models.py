from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام")
    age = models.CharField(max_length=70, verbose_name="سن")
    phoneNumber = models.CharField(max_length=300, verbose_name="شماره تلفن")
    email = models.EmailField(max_length=300, verbose_name="ایمیل")
    telegramId = models.CharField(max_length=100, verbose_name="تلگرام")
    graduation = models.CharField(max_length=300, verbose_name="تحصیلات")
    abilities = models.CharField(max_length=300, verbose_name="مهارت ها")
    address = models.CharField(max_length=300, verbose_name="آدرس")
    image = models.ImageField(upload_to='uploads', verbose_name="عکس")
    description = models.TextField(verbose_name="درباره من")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'خصوصیت'
        verbose_name_plural = 'اطلاعات شخصی'


class Abilities(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    experience = models.CharField(max_length=300, verbose_name='سابقه کار')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'توانایی'
        verbose_name_plural = 'توانایی ها'


class Projects(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    year = models.CharField(max_length=300, verbose_name='سال انشار')
    link = models.CharField(max_length=300, verbose_name='لینک')
    image = models.ImageField(upload_to='uploads/projects', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'


class Contact(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=300, verbose_name='موضوع' )
    message = models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:
        verbose_name = 'تماس با من'
        verbose_name_plural = 'لیست تماس با من'

    def __str__(self):
        return self.subject