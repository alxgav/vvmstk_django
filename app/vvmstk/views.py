from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from vvmstk.models import Groups_students, Students



def Main(request):
    return render(request, 'vvmstk/index.html')

# def Groups(request):


#     return render(request, 'vvmstk/groups.html')

class GroupsListView(ListView):
    model = Groups_students
    context_object_name = 'groups'
    template_name = 'vvmstk/groups.html'
    paginate_by = 8

    # def get_quertyset(self):
    #     return Groups_students.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = '4'
        return context
    
        

# class StudentListView(ListView):
#     model = Students
#     context_object_name = 'students'
#     template_name = 'vvmstk/students/students.html'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['now'] = Students.id_groups
#         return context


def student_list_view(request, pk):
    id = Students.objects.filter(id_groups=pk)
    return render(
        request, 
        'vvmstk/students/students.html',
        context={'students': id,
                 })


def groups_by_kategory(request, pk):
    kategory = Groups_students.objects.filter(kategory=pk)
    return render(
        request, 
        'vvmstk/groups.html',
        context={'students': kategory,
                 'kateg_B': 'B'})