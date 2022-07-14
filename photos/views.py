from django.shortcuts import render, redirect
from photos.models import Photo, Category
from django.conf import settings
from django.utils.translation import get_language

SEPARATOR = settings.SEPARATOR


def index(request):
    return render(request, 'index.html')


def links(request):
    return render(request, 'links.html')


def gallery(request):

    category = request.GET.get('category')
    if category is None:
        photos_preview = Photo.objects.order_by('-id')
    else:
        photos_preview = Photo.objects.filter(
            category__name_en=category).order_by('-id')

    categories = Category.objects.all()

    for ph in photos_preview:
        tmp = ph.image_url.split(SEPARATOR)
        for i in range(len(tmp)):
            tmp[i] = tmp[i].split('?')[0] + '?width=750&height=750&cropmode=none'
        ph.image_url = tmp
    return render(request, 'gallery.html', {'photos': photos_preview, 'categories': categories, 'language': get_language()})


def add(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        data = request.POST
        images = data['images']

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image_url=images,
            )

        return redirect('gallery')
    else:
        categories = Category.objects.all()
        context = {'categories': categories, 'separator': SEPARATOR}
        return render(request, 'add.html', context)


def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.image_url = photo.image_url.split(SEPARATOR)
    return render(request, 'photo.html', {'photo': photo, 'language': get_language()})
