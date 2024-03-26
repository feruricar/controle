from django.shortcuts import render
from .models import Produto
from django.urls import reverse_lazy

def produt_list(request):
    template_name = 'produt_list.html'
    objects=Produto.objects.all()
    context={'object_list':objects}
    return render(request, template_name,context)


def produt_detail(request,pk):
    template_name = 'produt_detail.html'
    obj=Produto.objects.get(pk=pk)
    context={'object':obj}
    return render(request, template_name,context)

def get_absolute_url(self):
    return reserve_lazy('produto:produto_detail',kwargs={'pk':self.pk}) 