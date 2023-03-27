from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import QueryDict
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Table_1
from .views import Table_1_form


@login_required
def act_edit_form(request, pkey):
    # TODO find out how to send less queries
    queryset = get_object_or_404(Table_1, pk=pkey)
    if request.user.type == 'DISPATCHER' or request.user.id == queryset.user_id:
        form = Table_1_form(instance=queryset)
        return render(request, 'acts/forms/edit-act-form.html', {'act': queryset, 'form': form})


@login_required
def act_edit(request, pkey):
    if request.method == 'PUT':
        # TODO find out how to send less queries
        queryset = get_object_or_404(Table_1, id=pkey)
        if request.user.type == 'DISPATCHER' or request.user.id == queryset.user_id:
            data = QueryDict(request.body).dict()
            form = Table_1_form(data, instance=queryset)
            if form.is_valid():
                form.save()
                Table_1.objects.filter(id=pkey).update(act_processing='Ожидание принятия заявки')
                return render(request, 'acts/details/act-detail.html', {'act': queryset})
            else:
                return render(request, 'acts/forms/edit-act-form.html', {'form': form})


def act_status(request):
    if request.user.type == 'DISPATCHER':
        status = request.GET.get('status')
        match status:
            case 'all':
                queryset = Table_1.objects.all().order_by('-date_updated')
            case 'completed':
                queryset = Table_1.objects.filter(completed=True)
            case 'uncompleted':
                queryset = Table_1.objects.filter(completed=False)
            case 'new':
                queryset = Table_1.objects.filter(act_processing='Ожидание принятия заявки')
            case 'expired':
                now = timezone.localtime(timezone.now())
                queryset = Table_1.objects.filter(do_until__lt=now).exclude(do_until=None)
            case _:
                queryset = Table_1.objects.all().order_by('-date_updated')

        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'acts/details/act-status.html', {'page_obj': page_obj, 'status': status})

# change type of request?
def accept_or_return_act(request, pkey):
    if request.user.is_staff == 1:
        status = request.GET.get('status')
        if status == 'accept':
            Table_1.objects.filter(id=pkey).update(act_processing='Заявки принята')
            button_status = 'Заявка принята'
        else:
            Table_1.objects.filter(id=pkey).update(act_processing='Заявка возвращена')
            button_status = 'Заявка возвращена'

        return render(request, 'acts/details/act-accept.html', {'button_title': button_status})
