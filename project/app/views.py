from django.views.generic import ListView
from .models import Laptop
from .forms import LaptopForm
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

# Create your views here.
def createorderview(request):
    form=LaptopForm()
    if request.method == "POST":
        form=LaptopForm(request.POST,request.FILES)
        if form.is_valid():
          form.save()
          return redirect('pagination')

    template_name='addorder.html'
    context={'form':form}
    return render(request,template_name,context)



class paginationview(ListView):
    paginate_by = 2
    model = Laptop
    template_name='pagination.html'