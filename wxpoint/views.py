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
        print(initmodelrun)
        cmrun = initmodelrun[0].run_name
        print(cmrun)
        """
        initimage = ModelImages.objects.filter(model_region__region='USA').filter(model_region__model_run__run_name=cmrun).filter(
            map_type="temps", timestep='00hr')
        """
        znitimage = ModelImages.objects.filter(model_region__model_run__currmodel__mname=post_data,
            model_region__model_run__run_name=cmrun,
            model_region__region='USA',
            map_type="temps", timestep='00hr')
        print(znitimage)
        #print(initimage[10].map_path.url)
        initimage = znitimage[0].map_path
        """
        allimages =  ModelImages.objects.filter(model_region__region='USA').filter(model_region__model_run__run_name=cmrun).filter(
            map_type="temps")
        """
        aimages = [x.map_path for x in znitimage]
        timages = [x.timestep for x in znitimage]
        #print(allimages)
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
        response_data['images'] = [timages , aimages]
        #print(response_data['images'])
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        cmrun = ModelRun.objects.all()
        cmrun = cmrun[len(cmrun)-1].run_name
        final = ModelImages.objects.filter(model_region__region='USA').filter(model_region__model_run__run_name=cmrun).filter(
            map_type="temps", timestep='00hr')
        starting_image = final[0].map_path
        #print(starting_image)
        return render(request, 'models.html', {'new_model_image': starting_image })

def model_page_buttons(request):
    pass
