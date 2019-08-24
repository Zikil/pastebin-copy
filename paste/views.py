from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from django.db.models import Q

from datetime import datetime
import datetime

from .models import *
from .forms import *

# pasteslist служит для списка паст для постоянного отображения на сайте
# Create your views here.

def pasteslist_get():  #список паст для постоянного отображения на сайте
    return Paste.objects.filter(Q(die_time__gt=datetime.datetime.now()) | Q(die_time__isnull=True), Q(access='public'))[:5]


def paste_list(request):  # вьюха для просмотра всех доступных паст
    pastes = Paste.objects.filter(Q(die_time__gt=datetime.datetime.now()) | Q(die_time__isnull=True))

    search_query = request.GET.get('search', '')
    if search_query:
        pastes = pastes.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        pastes = pastes.all()


    lenpaste = pastes.count()  # количество паст
    pasteslist = pasteslist_get()
    context = {
        'search_query': search_query,
        'pasteslist': pasteslist,
        'pastes': pastes,
        'lenpaste': lenpaste
    }
    return render(request, 'paste/pastes_list.html', context=context)


class PasteCreate(View):  # вьюха для создания новой пасты
    def get(self, request):
        form = PasteForm()
        pasteslist = pasteslist_get()
        context = {
            'pasteslist': pasteslist,
            'form': form
        }
        return render(request, 'paste/paste_create.html', context=context)

    def post(self, request):
        bound_form = PasteForm(request.POST)
        if bound_form.is_valid():
            print(dir(bound_form))
            new_paste = bound_form.save()
            if request.user.is_authenticated:
                new_paste.user = request.user
                new_paste.save()
            return redirect(new_paste)
        pasteslist = pasteslist_get()
        context = {
            'pasteslist': pasteslist,
            'form': bound_form
        }

        return render(request, 'paste/paste_create.html', context=context)


class PasteDetail(View):  # вьюха для просмотра отдельно каждой пасты
    def get(self, request, slug):
        paste = get_object_or_404(Paste, slug__iexact=slug)
        pasteslist = pasteslist_get()
        context = {
            'pasteslist': pasteslist,
            'paste': paste,
            # 'admin_paste': paste,
            # 'detail': True
        }
        if not(paste.die_time):
            return render(request, 'paste/paste_detail.html', context=context)
        else:
            if paste.die_time<datetime.datetime.now():
                return render(request, 'paste/paste_non_paste_detail.html', context=context)
            else:
                return render(request, 'paste/paste_detail.html', context=context)


class PasteDelete(View):  # вьюха для удаления пасты
    def get(self, request, slug):
        paste = get_object_or_404(Paste, slug__iexact=slug)
        pasteslist = pasteslist_get()
        context = {
            'pasteslist': pasteslist,
            'paste': paste
        }
        return render(request, 'paste/paste_delete.html', context=context)

    def post(self, request, slug):
        paste = get_object_or_404(Paste, slug__iexact=slug)
        paste.delete()
        return redirect(reverse('paste_list_url'))
