from django.shortcuts import render
from contact.models import Query
from Home.models import Count
import datetime
# Create your views here.
def main_page(request):
    count = Count.objects.get(name__iexact="main")
    date = datetime.datetime.now()
    data = {'count':count.visitors, 'year':date.year}
    
    count.visitors += 1
    count.save()
    
    if request.method == "POST":
        try:
            Name = request.POST['Name']
            Email = request.POST['Email']
            Desc = request.POST['Desc']

            new_q = Query.objects.create(Name=Name, Email=Email, Desc=Desc)
            new_q.save()
        except Exception as e:
            print(e)
    return render(request, "index.html", data)