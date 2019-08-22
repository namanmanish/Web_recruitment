from django.shortcuts import render,redirect
from .models import Person,State,City,College
from .forms import PersonForm
from django.http import JsonResponse

def index(request):
 people = Person.objects.all()   
 contex = {'people': people }
 return render(request,'music/index.html',contex)

def detailes(request,person_id):
  a = Person.objects.all()
  contex = {'c': a,'b': person_id}
  return render(request,'music/detailes.html',contex)
 
def statistics(request):
 sum=0
 count=0
 count1=0
 a=[0]*len(State.objects.all())
 b=[0]*len(College.objects.all())
 c=[0]*len(City.objects.all())
 for person in Person.objects.all():
  sum=sum+person.age
  count=count+1
  count1=0
  for state in State.objects.all():
   if (state.name==person.state):
    a[count1]=a[count1]+1
    break 
   else:
    count1=count1+1
  count1=0
  for college in College.objects.all():
   if (college.name==person.college):
    b[count1]=b[count1]+1
   else:
    count1=count1+1
  count1=0
  for city in City.objects.all():
   if (city.name==person.city):
    c[count1]=c[count1]+1
   else:
    count1=count1+1 
 avarage=sum/count
 i=0
 d=['']*len(State.objects.all())
 e=['']*len(College.objects.all())
 f=['']*len(City.objects.all())
 for state in State.objects.all():
  a[i]=a[i]*100/count
  d[i] = state.name + " : " + str(a[i])
  i=i+1
 i=0
 for college in College.objects.all():
  b[i]=b[i]*100/count
  e[i] = college.name + " : " + str(b[i])
  i=i+1
 i=0
 for city in City.objects.all():
  c[i]=c[i]*100/count
  f[i] = city.name + " : " + str(c[i])
  i=i+1
 r=0
 contex = { 's': d,'ci': f, 'co': e, 'avr': avarage, 'z': count}
 return render(request,'music/statistics.html',contex)
def new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/music') 
    else:
         form = PersonForm()
         return render(request, 'music/new.html', {'form': form})
def ajax(request):
 state_id=request.GET.get('state_id')
 cities=City.objects.filter(state_name=state_id)
 data = {'cities': cities}
 return JsonResponse(data)
    
  
