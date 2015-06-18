from django.shortcuts import render
from django.http import HttpResponse
from wxpoint.models import NModels, ModelRun, ModelRegion, ModelImages
import json

def home_page(request):
        return render(request, 'home.html')

def model_page(request):
    if request.method =='POST':

        post_data = request.POST.get('initmdls')
        print(post_data)
        initmodelrun = ModelRun.objects.filter(currmodel__mname=post_data)
        cmrun = initmodelrun[0].run_name
        initimage = ModelImages.objects.filter(model_region__region='USA').filter(model_region__model_run__run_name=cmrun).filter(
            map_type="temps", timestep='00hr')
        initimage = initimage[10].map_path
        print(initimage)
        """
        new_model_image = request.POST['model']
        gfsmodel = NModels.objects.create(mname=new_model_image)
        currentmodelrun = ModelRun.objects.create(currmodel=gfsmodel, run_name='gfs12z')
        currentmodelregion = ModelRegion.objects.create(model_run=currentmodelrun, region='USA')
        myimage = ModelImages.objects.create(model_region=currentmodelregion, map_type="temps", 
            map_path='/static/images/GFS2mt18z.gif', timestep="00hr")
        """
        #test return
        response_data = {}
        response_data['result'] = initimage
        return HttpResponse(json.dumps(response_data),content_type="application/json")
        #return HttpResponse(request, 'models.html', {'new_model_image': myimage.map_path,
        #                'modeltime':myimage.timestep })
        
    else:
        cmrun = ModelRun.objects.all()
        cmrun = cmrun[len(cmrun)-1].run_name
        final = ModelImages.objects.filter(model_region__region='USA').filter(model_region__model_run__run_name=cmrun).filter(
            map_type="temps", timestep='00hr')
        starting_image = final[0].map_path
        #print(starting_image)
        return render(request, 'models.html', {'new_model_image': starting_image })
