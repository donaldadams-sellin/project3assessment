from django.shortcuts import redirect, render
from .models import Widget
from .forms import WidgetForm
# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    return render(request, 'index.html', {'widgets':widgets, 'form':form})

def add_widget(request):
    widget = WidgetForm(request.POST)
    if widget.is_valid():
        widget.save()
        return redirect('index')
    return redirect('index')