from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from .models import Table_1,Table_2,Table_3,Table_4,Table_5,Table_6
from .forms import Table_1_form,Table_2_form,Table_3_form,Table_4_form,Table_5_form,Table_6_form

def tables(request):

    return render(request, 'acts/tables.html', {})

def tables_first(request, pkey):
    if request.user.type == 'DISPATCHER':
        queryset = Table_1.objects.select_related('user').filter(user_id=pkey)
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_first.html', {'page_obj': page_obj})

def tables_second(request, pkey):
    if request.user.type == 'DISPATCHER':
        queryset = Table_1.objects.select_related('user').filter(user_id=pkey)
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_second.html', {'page_obj': page_obj})



def table_first(request):

    return render(request, 'acts/tables.html', {})


def table_second(request):

    return render(request, 'acts/tables.html', {})

















@login_required
def acts(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_1.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_1.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/act_list.html', {'page_obj': page_obj})

@login_required
def tables_1(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_1.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_1.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_first.html', {'page_obj': page_obj})

@login_required
def tables_2(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_2.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_2.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_second.html', {'page_obj': page_obj})

@login_required
def tables_3(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_3.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_3.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_third.html', {'page_obj': page_obj})

@login_required
def tables_4(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_4.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_4.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_fourth.html', {'page_obj': page_obj})

@login_required
def tables_5(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_5.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_5.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_fifth.html', {'page_obj': page_obj})

@login_required
def tables_6(request):
    if request.user.type == 'DISPATCHER':
        queryset = Table_6.objects.select_related('user').all().order_by('-date_updated')
    else:
        queryset = Table_6.objects.select_related('user').filter(
            user_id=request.user.id)  # request.session.get('_auth_user_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'acts/tables_sixth.html', {'page_obj': page_obj})


@login_required
def create_1(request):
    if request.method == 'GET':
        form = Table_1_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"
        return render(request, 'acts/create_act.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_1_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act.html', {'form': form})

@login_required
def create_2(request):
    if request.method == 'GET':
        form = Table_2_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"

        return render(request, 'acts/create_act_2.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_2_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act_2.html', {'form': form})

@login_required
def create_3(request):
    if request.method == 'GET':
        form = Table_3_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"
        return render(request, 'acts/create_act_3.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_3_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act_3.html', {'form': form})

@login_required
def create_4(request):
    if request.method == 'GET':
        form = Table_4_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"
        return render(request, 'acts/create_act_4.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_4_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act_4.html', {'form': form})

@login_required
def create_5(request):
    if request.method == 'GET':
        form = Table_5_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"
        return render(request, 'acts/create_act_5.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_5_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act_5.html', {'form': form})

@login_required
def create_6(request):
    if request.method == 'GET':
        form = Table_6_form()
        message = "Журналы входящие в международные базы цитируемых журналов Web of Science и Scopus"
        return render(request, 'acts/create_act_6.html', {'form': form, 'message':message})

    elif request.method == 'POST':
        form = Table_6_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/acts/')
        else:
            return render(request, 'acts/create_act_6.html', {'form': form})


@login_required
def act(request, pkey):
    queryset = get_object_or_404(Table_1, pk=pkey)
    if request.user.type == 'DISPATCHER' or request.user.id == queryset.user_id:
        return render(request, 'acts/act.html', {'act': queryset})
    else:
        return render(request, 'no_access.html')


def act_search(request):
    if request.user.type == 'DISPATCHER':
        if request.method == 'POST':
            # any orm injections?
            search = request.POST['search']
            acts = Table_1.objects.all()
            queryset = [act for act in acts if (
                    (search.lower() in act.title.lower())
                    or
                    (search.lower() in act.adress.lower())
                    or
                    (search.lower() in act.text.lower()))
                        ]

            paginator = Paginator(queryset, 10)
            page_obj = paginator.get_page(None)
            return render(request, 'acts/details/act-search.html', {'page_obj': page_obj, 'search': search})

        if request.method == 'GET':
            search = request.GET['search']
            acts = Table_1.objects.all()
            queryset = [act for act in acts if (
                    (search.lower() in act.title.lower())
                    or
                    (search.lower() in act.adress.lower())
                    or
                    (search.lower() in act.text.lower()))
                        ]

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'acts/details/act-search.html', {'page_obj': page_obj, 'search': search})



