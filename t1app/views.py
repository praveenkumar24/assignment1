from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.core import serializers
#from . models import Myimg
#from . serializers import MyimgSerial
from django.shortcuts import render, redirect
#from django.shortcuts import render_to_response
from . forms import *
import pickle
import joblib
import json
from sklearn import preprocessing
from torchvision import transforms
import torch
import numpy as np
import io
from PIL import Image
import shutil

from django.views.generic import TemplateView


#class HomePageView(TemplateView):
#    template_name = "firstind.html"
# Create your views here.
def photo_image_view(request):

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('success')
    else:
        form = PhotoForm()
    return render(request, 'firstind.html', {'form' : form})


def success(request):
#    try:
    mdl=joblib.load("/Users/Praveen/Desktop/MP/trail/T1/t1app/lens.pkl")
        #if request.method == 'POST':
    #form = PhotoForm(request.POST, request.FILES)

      #img1=Image.open(request.FILES['imge'])
    img1=Image.open(r'C:\Users\Praveen\Desktop\MP\trail\T1\media\images\Newnameimg.png').convert('RGB')
        #img1=transforms.ToPILImage()(img1)
        #img1 = Image.convert(img1)
        #img1 = np.array(img1)
    preprocess = transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224),transforms.RandomHorizontalFlip(),transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])
    img_preprocessed = preprocess(img1)
    batch_img_tensor = torch.unsqueeze(img_preprocessed, 0)
    out=mdl(batch_img_tensor)
    with open(r'C:\Users\Praveen\Desktop\MP\trail\T1\t1app\imagenet_classes.txt')as f:
        labels = [line.strip() for line in f.readlines()]
    _, index = torch.max(out, 1)
        #percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        #labels[index[0]])
    #form = PhotoForm(request.POST, request.FILES)
    #form.delete()
    #obj=Photo.objects.get(pk=1)
    #obj.Photo_Img.delete()
    shutil.rmtree('C:/Users/Praveen/Desktop/MP/trail/T1/media/images')
    res=str(labels[index[0]])
    con={}
    con['res']=res
    return render(request,'results.html',con) # Redirect after POST
    #return HttpResponse('Object is {}'.format(labels[index[0]]))
        #return HttpResponse('successfully uploaded')
    #except FileNotFoundError as e:
    #    return HttpResponse(e.args[0], status.HTTP_400_BAD_REQUEST)

def base_layout(request):
	template='base.html'
	return render(request,template)

def delete(self, *args, **kwargs):
    self.Photo_Image.storage.delete(self.Photo_Image.name)
    super(Photo,self).delete(*args, **kwargs)
