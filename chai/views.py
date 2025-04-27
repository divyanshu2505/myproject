from django.shortcuts import render

#Create  first view
def all_chai(request):
    return render(request, 'chai/all_chai.html')