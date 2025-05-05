from django.shortcuts import render

def test_app(request):
    return render(request,'test_app/index.html')
# Create your views here.
def about(request):
    return render(request,'test_app/about.html')