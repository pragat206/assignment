from django.shortcuts import render
from . import forms
from .forms import Main
from.models import UrlData
import random
import string
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def Shortening(request):
    if request.method == 'POST':
        form = Main(request.POST)
        if form.is_valid():
            short = ''.join(random.choice(string.ascii_letters)for x in range(10))
            url = form.cleaned_data['url']
            new_url = UrlData(url = url,short = short)
            request.user.urlshort.add(new_url)
            return redirect('/')
    else:
        form = Main()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)

def Redirect(request, shorts):
    data = UrlData.objects.get(short = shorts)
    return redirect(data.url)
