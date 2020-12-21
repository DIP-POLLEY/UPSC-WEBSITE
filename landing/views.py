from django.shortcuts import render
from .models import Practice1,Practice2,GS1_Current,GS1_static,GS2_Current,GS2_static,GS3_Current,GS3_static,GS4_Current,GS4_static,Essay,Sociology_current,Sociology_static

# Create your views here.
def index(request):

    ps1 = Practice1.objects.all()
    ps2 = Practice2.objects.all()
    
    gs1 = GS1_static.objects.all()
    gc1 = GS1_Current.objects.all()

    gs2 = GS2_static.objects.all()
    gc2 = GS2_Current.objects.all()

    gs3 = GS3_static.objects.all()
    gc3 = GS3_Current.objects.all()

    gs4 = GS4_static.objects.all()
    gc4 = GS4_Current.objects.all()

    
    esy = Essay.objects.all()

    ss = Sociology_static.objects.all()
    sc = Sociology_current.objects.all()    

    return render(request,"index.html",{'obj': ps1,'obj2': ps2,'obj3':gs1,'obj4':gc1, 'obj5': gs2, 'obj6':gc2, 'obj7':gs3,'obj8':gc3, 'obj9':gs4, 'obj10':gc4, 'obj11':esy, 'obj12':ss, 'obj13':sc})
