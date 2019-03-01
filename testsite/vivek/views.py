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
          client= request.GET.get('cname')
          f = open( '/root/django/testsite/files/hostname', 'w+' )
          f.write( hostname )
          f.close()           
          f = open( '/root/django/testsite/files/clientname', 'w+' )
          f.write( client )
          f.close()           
          import os
          cmd = 'ansible-playbook /root/django/testsite/files/hostname.yml'
          os.system(cmd)
          return HttpResponse('Hostname changed')

def take_view(request):
          package = request.GET.get('install')
          client= request.GET.get('cname')
          f = open( '/root/django/testsite/files/indata', 'w+' )
          f.write( package )
          f.close() 
          f = open( '/root/django/testsite/files/clientname', 'w+' )
          f.write( client )
          f.close()           
          import os
          cmd = 'ansible-playbook /root/django/testsite/files/install.yml'
          os.system(cmd)

          return HttpResponse('Package installed')

