from django.shortcuts import render
from django.http import HttpResponse
from wxpoint.models import NModels, ModelRun, ModelRegion, ModelImages

def home_page(request):
        return render(request, 'home.html')

def model_page(request):
    if request.method =='POST':
        new_model_image = request.POST['GFS']
        gfsmodel = NModels.objects.create(mname=new_model_image)
        currentmodelrun = ModelRun.objects.create(currmodel=gfsmodel, run_name='gfs00z')
        currentmodelregion = ModelRegion.objects.create(model_run=currentmodelrun, region='USA')
        myimage = ModelImages.objects.create(model_region=currentmodelregion, map_type="temps", 
            map_path='/static/images/GFS2mt12z.gif', timestep="00hr")
        return render(request, 'models.html', {'new_model_image': myimage.map_path, })
    return render(request, 'models.html')
