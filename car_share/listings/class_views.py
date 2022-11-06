from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ListingsModel

class ListingsView(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('-updated')
        context = {'tasks':tasks}
        return render(request, 'base/index.html', context)

    def post(self, request):
        task = Task.objects.create(body=request.POST.get('body'))
        task.save()
        return redirect('tasks')



class ListingsViewsCreate(CreateView):
    model = ListingsModel

class ListingsViewsDelete(DeleteView):
    model = ListingsModel
    context_object_name: str
