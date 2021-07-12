from django.shortcuts import render
from contact.models import Query
# Create your views here.
def main_page(request):
    if request.method == "POST":
        try:
            Name = request.POST['Name']
            Email = request.POST['Email']
            Desc = request.POST['Desc']

            new_q = Query.objects.create(Name=Name, Email=Email, Desc=Desc)
            new_q.save()
        except Exception as e:
            print(e)
    return render(request, "index.html")