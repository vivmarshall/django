from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from .forms import NameForm
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
          hostname= request.GET.get('hostname')
          f = open( '/root/ansible/hostname', 'w+' )
          f.write( hostname )
          f.close()           
          import os
          cmd = 'ansible-playbook /root/ansible/hostname.yml'
          os.system(cmd)
          return HttpResponse('Hostname changed')

def take_view(request):
          package = request.GET.get('install')
          f = open( '/root/ansible/indata', 'w+' )
          f.write( package )
          f.close() 
          import os
          cmd = 'ansible-playbook /root/ansible/install.yml'
          os.system(cmd)

          return HttpResponse('Package installed')

