from django.shortcuts import render

def test_app(request):
    data = {
        'title':'test page',
        'values':['some','hello','123'],
        'obj':{
            'car':'bmw',
            'age':18,
            'hobby':'games'
        }
    }
    return render(request,'test_app/index.html', data)
# Create your views here.
def about(request):
    return render(request,'test_app/about.html')