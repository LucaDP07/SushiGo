from django.shortcuts import render

def all_dishes(request):
    """ A view to show all dishes, including sorting and search queries """

    dishes = Dish.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)
