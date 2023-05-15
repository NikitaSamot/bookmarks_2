from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm, ImageUpdateForm
from .models import Image


# Create your views here.


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Фото успешно добавлено')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


def edit_images(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    if request.method == 'POST':
        form = ImageUpdateForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            images = Image.objects.all()
            for image in images:
                image.url = url
                image.title = title
                image.description = description
                image.save()
            return redirect(images.get_absolute_url())
    else:
        form = ImageUpdateForm()
    return render(request, 'images/image/edit_images.html', {'form': form})
