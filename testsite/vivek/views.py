from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from .forms import NameForm
from django.core.files.base import ContentFile
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
	
        return render(request, 'index.html', context=None)

class hostpage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'host.html', context=None)

class installpage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'install.html', context=None)


def my_view1(request):
        if request.method == 'POST':
          
          hostname = request.POST.get('hostname')
          import os
          os.system('echo $hostname > /root/ansible/hostname')
          cmd = 'ansible-playbook /root/ansible/hostname.yml'
          os.system(cmd)
 
        return HttpResponse('Hostname changed')

def take_view(request):
        if request.method == 'POST':
          package = request.POST.get('install')
          import os
          os.system('echo $package > /root/ansible/hostname')
          cmd = 'ansible-playbook /root/ansible/install.yml'
          os.system(cmd)

        return HttpResponse('Package installed')

