from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "index.html")
def submitted(request):
    print("Got Survey Info.......")
    name_from_survey = request.POST['name']
    location_from_survey = request.POST['location']
    lang_from_survey = request.POST['language']
    comment_from_survey = request.POST['comment']
    print(name_from_survey, location_from_survey, lang_from_survey, comment_from_survey)
    context = {
        "name_on_survey" : name_from_survey,
        "location_on_survey" : location_from_survey,
        "lang_on_survey" : lang_from_survey,
        "comment_on_survey" : comment_from_survey,

    }
    return render(request, "form_done.html",context)
