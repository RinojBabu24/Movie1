from django.shortcuts import redirect, render
 
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def demo(request):
    mov=Movie.objects.all()
    return render(request,'index.html',{'movie':mov})


def demo1(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Year = request.POST['Year']
        Description = request.POST['Description']
        img = request.FILES['img']

        movies=Movie(
            Name=Name,  
            Year=Year,
            Description=Description,
            img=img
        )
        movies.save()
       
        return redirect('fapp:demo')
    return render(request,'home.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('fapp:demo')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('fapp:demo')
    return render(request,'delete.html')


