from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView
from vvmstk.models import Groups_students


def Main(request):
    return render(request, 'vvmstk/index.html')

# def Groups(request):


#     return render(request, 'vvmstk/groups.html')

class GroupsListView(ListView):
    model = Groups_students
    context_object_name = 'groups'
    template_name = 'vvmstk/groups.html'

    # def get_quertyset(self):
    #     return Groups_students.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = '4'
        return context
        