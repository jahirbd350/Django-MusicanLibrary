from django.shortcuts import render, redirect
from . import forms
from .models import Musician


def add_musician(request):
    if request.method == 'POST':
        musician = forms.MusicianForm(request.POST)
        musician.save()
        return redirect('add_musician')
    else:
        musician = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    print(musician)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    return render(request, "add_musician.html", {'form': musician_form})
