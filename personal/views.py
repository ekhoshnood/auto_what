from django.shortcuts import render
from .models import Question

# Create your views here.
def personal_page(request):
    ##first way
    # context = {}
    # context['some_string'] = "this is the context string that's been pass to html"
    # context['some_number'] = 13900404
    # return render(request, "personal/personal_home_screen.html", context)


    ##second way
    # context = {
    #     'some_string' : "this is the context string that's been pass to html",
    #     'some_number' : 13900404
    # }
    # return render(request, "personal/personal_home_screen.html", context)


    ##another thing
    # list_of_values = []
    # list_of_values.append("first")
    # list_of_values.append("second")
    # list_of_values.append("third")
    # list_of_values.append("fourth")
    # list_of_values.append("fifth")
    #
    # context = {}
    # context['my_list'] = list_of_values
    # return render(request, "personal/personal_home_screen.html", context)


    ## quering data base data table inside view and pass to template
    questions = Question.objects.all()
    context = {}
    context['questions'] = questions
    return render(request, "personal/personal_home_screen.html", context)
