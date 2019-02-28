from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
def my_view1(request):
        if request.method == 'GET':
          import os
          cmd = 'ansible-playbook /root/ansible/hostname.yml'
          os.system(cmd)
 
        return HttpResponse('Hostname changed')

def my_view2(request):
        if request.method == 'GET':
          import os
          cmd = 'ansible-playbook /root/ansible/install.yml'
          os.system(cmd)

        return HttpResponse('Hello, welcome to the index page.')

