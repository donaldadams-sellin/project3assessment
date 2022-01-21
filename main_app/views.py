from django.shortcuts import redirect, render
from django.db.models import Count
from .models import Widget
from .forms import WidgetForm
# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    total_quant = 0
    for widget in widgets:
        total_quant += widget.quantity
    return render(request, 'index.html', {'widgets':widgets, 'form':form, 'total_quant': total_quant})

def add_widget(request):
    widget = WidgetForm(request.POST)
    if widget.is_valid():
        widget.save()
        return redirect('index')
    return redirect('index')

def remove_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')