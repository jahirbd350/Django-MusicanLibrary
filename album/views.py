from django.shortcuts import render, redirect
from . import forms
from .models import Album
# Create your views here.


def add_album(request):
    if request.method == 'POST':
        album = forms.AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect("add_album")
    else:
        album = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album})


def del_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("homepage")


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    print(album)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")
    return render(request, 'add_album.html', {'form': album_form})
