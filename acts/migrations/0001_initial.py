# Generated by Django 4.0.4 on 2023-03-29 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title_of_table', models.CharField(max_length=300, verbose_name='Участие в научных проектах ')),
                ('title', models.CharField(max_length=300, verbose_name='Название проекта ИРН')),
                ('title2', models.CharField(max_length=300, verbose_name='Запрашиваемая Сумма ')),
                ('title3', models.CharField(max_length=300, verbose_name='Период участия в проекте')),
                ('title4', models.CharField(max_length=300, verbose_name='Участие в проектах в рамках программно-целевого финансирования')),
                ('title5', models.CharField(max_length=300, verbose_name='Участие в проектах в рамках  грантового финансирования')),
                ('title6', models.CharField(max_length=300, verbose_name='Участие в международных научно-исследовательских проектах / программах  ')),
                ('title7', models.CharField(max_length=300, verbose_name='Участия в проектах по коммерциализации, внедрению ипродвижению научных результатов,финансируемых из ')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Подтверждающий документ прикрепить')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Table_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title_of_table', models.CharField(max_length=300, verbose_name='Свидетельство о государственной регистрации прав на объект авторского права')),
                ('title', models.CharField(max_length=300, verbose_name='Название Свидетельства')),
                ('data', models.CharField(max_length=300, verbose_name='Данные о свидетельстве (номер, дата, год)')),
                ('authors', models.CharField(max_length=300, verbose_name='Авторы')),
                ('author_type', models.CharField(max_length=300, verbose_name='Тип автора')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Копия свидетельства о государственной регистрации прав на объект авторского права')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Table_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title_of_table', models.CharField(max_length=300, verbose_name='Статьи опубликованные в сборниках конференции')),
                ('title', models.CharField(max_length=300, verbose_name='Название статьи')),
                ('co_creators', models.CharField(max_length=300, verbose_name='Соавторы')),
                ('author_type', models.CharField(max_length=300, verbose_name='Тип автора')),
                ('number_of_authors', models.CharField(max_length=300, verbose_name='Количество авторов')),
                ('journal_title', models.CharField(max_length=300, verbose_name='Название журнала, номер, год выпуска ')),
                ('conf', models.CharField(max_length=300, verbose_name='конференции международные,республиканские(название сборника, месяц, год)')),
                ('int', models.CharField(max_length=300, verbose_name='международные,республиканские')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Оттиск прикрепить')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Table_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title_of_table', models.CharField(max_length=300, verbose_name='Журналы входящие в Рецензирумые зарубежные журналы рекомендуемые КОКСНВО')),
                ('title', models.CharField(max_length=300, verbose_name='Название статьи')),
                ('co_creators', models.CharField(max_length=300, verbose_name='Соавторы')),
                ('author_type', models.CharField(max_length=300, verbose_name='Тип автора')),
                ('number_of_authors', models.CharField(max_length=300, verbose_name='Количество авторов')),
                ('journal_title', models.CharField(max_length=300, verbose_name='Название журнала, номер, год выпуска ')),
                ('kokson', models.CharField(max_length=300, verbose_name='Наличие статьи в перечне,  рекомендуемые КОКСНВО РК ')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Оттиск прикрепить')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Table_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title_of_table', models.CharField(max_length=300, verbose_name='Журналы входящие в Рецензирумые зарубежные журналы (РИНЦ)')),
                ('title', models.CharField(max_length=300, verbose_name='Название статьи')),
                ('co_creators', models.CharField(max_length=300, verbose_name='Соавторы')),
                ('author_type', models.CharField(max_length=300, verbose_name='Тип автора')),
                ('number_of_authors', models.CharField(max_length=300, verbose_name='Количество авторов')),
                ('journal_title', models.CharField(max_length=300, verbose_name='Название журнала, номер, год выпуска ')),
                ('rinc', models.CharField(max_length=300, verbose_name='Наличие статьи в базах РИНЦ')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Оттиск прикрепить')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Table_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('co_creators', models.CharField(max_length=100, verbose_name='Соавторы')),
                ('author_first', models.CharField(max_length=100, verbose_name='Первый автор')),
                ('number_of_authors', models.CharField(max_length=100, verbose_name='Количество авторов')),
                ('journal_title', models.CharField(max_length=100, verbose_name='Название журнала, номер, год выпуска ')),
                ('percentile', models.CharField(max_length=100, verbose_name='Процентиль  (1..100 по Scopus) или квартиль (Q1..Q4 по WoS)')),
                ('url', models.CharField(max_length=100, verbose_name='DOI статьи')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files', verbose_name='Оттиск прикрепить')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
    ]
