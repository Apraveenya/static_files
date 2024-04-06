from django.shortcuts import render

# Create your views here.
def styles(request):
    return render(request,'styles.html')
def style1(request):
    return render(request,'style1.html')
def animation(request):
    return render(request,'animation.html')

