from django.shortcuts import render
from account.models import Account


def course_training_page(request):
    context         = {}

    accounts        = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "base.html", context)
