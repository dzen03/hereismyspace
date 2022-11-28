from django.http import Http404
from django.shortcuts import render, redirect

import photos.models
from photos.models import Photo, Category
from django.conf import settings
from django.utils.translation import get_language

SEPARATOR = settings.SEPARATOR


def index(request):
    return render(request, 'index.html')


def links(request):
    return render(request, 'links.html')


def gallery(request):
    photos_preview = Photo.objects.order_by('-id')
    categories = Category.objects.all()

    for ph in photos_preview:
        tmp = ph.image_url.split(SEPARATOR)
        for i in range(len(tmp)):
            tmp[i] = tmp[i].split('?')[0] + '?width=750&height=750&cropmode=none'
        ph.image_url = tmp
    return render(request, 'gallery.html', {'photos': photos_preview, 'categories': categories,
                                            'language': get_language()})


def gallery_filter(request, filter):

    photos_preview = Photo.objects.filter(
            category__name_en=filter).order_by('-id')
    categories = Category.objects.all()

    for ph in photos_preview:
        tmp = ph.image_url.split(SEPARATOR)
        for i in range(len(tmp)):
            tmp[i] = tmp[i].split('?')[0] + '?width=750&height=750&cropmode=none'
        ph.image_url = tmp
    return render(request, 'gallery.html', {'photos': photos_preview, 'categories': categories,
                                            'language': get_language()})

def add(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        data = request.POST
        images = data['images']

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new_en'] != '':
            category, created = Category.objects.get_or_create(
                name_en=data['category_new_en'],
                name_ru=data['category_new_ru'],
            )
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description_en=data['description_en'],
            description_ru=data['description_ru'],
            camera_name=data['camera_name'],
            shutter_speed=data['shutter_speed'],
            focal_length=data['focal_length'],
            aperture=data['aperture'],
            image_url=images,
        )

        return redirect('gallery')
    else:
        categories = Category.objects.all()
        context = {'categories': categories, 'separator': SEPARATOR, 'language': get_language()}
        return render(request, 'add.html', context)


def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        data = request.POST
        images = data['images']

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new_en'] != '':
            category, created = Category.objects.get_or_create(
                name_en=data['category_new_en'],
                name_ru=data['category_new_ru'],
            )
        else:
            category = None

        Photo.objects.filter(id=pk).update(
            category=category,
            description_en=data['description_en'],
            description_ru=data['description_ru'],
            camera_name=data['camera_name'],
            shutter_speed=data['shutter_speed'],
            focal_length=data['focal_length'],
            aperture=data['aperture'],
            image_url=images,)

        return redirect('gallery')
    else:
        categories = Category.objects.all()
        try:
            data = Photo.objects.get(id=pk)
        except photos.models.Photo.DoesNotExist:
            raise Http404("Post not found")
        context = {'categories': categories, 'separator': SEPARATOR, 'language': get_language(), 'data': data}
        return render(request, 'add.html', context)


def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    tmp = photo.image_url.split(SEPARATOR)
    for i in range(len(tmp)):
        tmp[i] = tmp[i].split('?')[0] + '?width=3000&height=2000&cropmode=none'
    photo.image_url = tmp
    return render(request, 'photo.html', {'photo': photo, 'language': get_language()})
