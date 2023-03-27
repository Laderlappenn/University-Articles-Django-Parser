from django.db import models
from django.conf import settings
from django.utils import timezone
# from accounts.models import Account

class Table_1(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # executer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='acts_executer')
    # user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, verbose_name="Название статьи")
    co_creators = models.CharField(max_length=100, verbose_name="Соавторы")
    author_type = models.CharField(max_length=100, verbose_name="Тип автора")
    number_of_authors = models.CharField(max_length=100, verbose_name="Количество авторов")
    journal_title = models.CharField(max_length=100, verbose_name="Название журнала, номер, год выпуска ")
    percentile = models.CharField(max_length=100, verbose_name="Процентиль  (1..100 по Scopus) или квартиль (Q1..Q4 по WoS)")
    url = models.CharField(max_length=100, verbose_name="DOI статьи")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files', verbose_name ="Оттиск прикрепить")

    class Meta:
        ordering = ['date_updated']
        # indexes = [models.Index(fields=['fieldname1', 'fieldname1']), ]


    # # signals did it
    # @property
    # def change_on_update(self):
    #     if self.pk:
    #         old_date_updated = Act.objects.get(pk=self.pk).date_updated
    #         if old_date_updated != self.date_updated:
    #             # do something here
    #             user_id = Act.objects.get(pk=self.pk).user_id
    #             profile = Account.objects.get(pk=user_id)
    #             profile.date_updated = timezone.now()
    #             profile.save()

    def __str__(self):
        return self.title

class Table_2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title_of_table = models.CharField(max_length=300,
                                      verbose_name="Журналы входящие в Рецензирумые зарубежные журналы (РИНЦ)")
    title = models.CharField(max_length=300, verbose_name="Название статьи")
    co_creators = models.CharField(max_length=300, verbose_name="Соавторы")
    author_type = models.CharField(max_length=300, verbose_name="Тип автора")
    number_of_authors = models.CharField(max_length=300, verbose_name="Количество авторов")
    journal_title = models.CharField(max_length=300, verbose_name="Название журнала, номер, год выпуска ")
    rinc = models.CharField(max_length=300,
                                  verbose_name="Наличие статьи в базах РИНЦ")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files', verbose_name="Оттиск прикрепить")

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.title

class Table_3(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title_of_table = models.CharField(max_length=300,
                                      verbose_name="Журналы входящие в Рецензирумые зарубежные журналы рекомендуемые КОКСНВО")
    title = models.CharField(max_length=300, verbose_name="Название статьи")
    co_creators = models.CharField(max_length=300, verbose_name="Соавторы")
    author_type = models.CharField(max_length=300, verbose_name="Тип автора")
    number_of_authors = models.CharField(max_length=300, verbose_name="Количество авторов")
    journal_title = models.CharField(max_length=300, verbose_name="Название журнала, номер, год выпуска ")
    kokson = models.CharField(max_length=300,
                            verbose_name="Наличие статьи в перечне,  рекомендуемые КОКСНВО РК ")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files',
                            verbose_name="Оттиск прикрепить")

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.title

class Table_4(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title_of_table = models.CharField(max_length=300,
                                      verbose_name="Статьи опубликованные в сборниках конференции")
    title = models.CharField(max_length=300, verbose_name="Название статьи")
    co_creators = models.CharField(max_length=300, verbose_name="Соавторы")
    author_type = models.CharField(max_length=300, verbose_name="Тип автора")
    number_of_authors = models.CharField(max_length=300, verbose_name="Количество авторов")
    journal_title = models.CharField(max_length=300, verbose_name="Название журнала, номер, год выпуска ")
    conf = models.CharField(max_length=300,
                            verbose_name="конференции международные,республиканские(название сборника, месяц, год)")
    int = models.CharField(max_length=300,
                            verbose_name="международные,республиканские")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files',
                            verbose_name="Оттиск прикрепить")

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.title


class Table_5(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title_of_table = models.CharField(max_length=300,
                                      verbose_name="Свидетельство о государственной регистрации прав на объект авторского права")
    title = models.CharField(max_length=300, verbose_name="Название Свидетельства")
    data = models.CharField(max_length=300, verbose_name="Данные о свидетельстве (номер, дата, год)")
    authors = models.CharField(max_length=300, verbose_name="Авторы")
    author_type = models.CharField(max_length=300, verbose_name="Тип автора")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files',
                            verbose_name="Копия свидетельства о государственной регистрации прав на объект авторского права")

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.title

class Table_6(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title_of_table = models.CharField(max_length=300,
                                      verbose_name="Участие в научных проектах ")
    title = models.CharField(max_length=300, verbose_name="Название проекта ИРН")
    title2 = models.CharField(max_length=300, verbose_name="Запрашиваемая Сумма ")
    title3 = models.CharField(max_length=300, verbose_name="Период участия в проекте")
    title4 = models.CharField(max_length=300, verbose_name="Участие в проектах в рамках программно-целевого финансирования")
    title5 = models.CharField(max_length=300, verbose_name="Участие в проектах в рамках  грантового финансирования")
    title6 = models.CharField(max_length=300, verbose_name="Участие в международных научно-исследовательских проектах / программах  ")
    title7 = models.CharField(max_length=300, verbose_name="Участия в проектах по коммерциализации, внедрению ипродвижению научных результатов,финансируемых из ")
    file = models.FileField(null=True, blank=True, upload_to='files/act_files',
                            verbose_name="Подтверждающий документ прикрепить")

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.title
