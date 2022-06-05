from django.shortcuts import render


def Main(request):
    return render(request, 'vvmstk/index.html')

def Groups(request):
    return render(request, 'vvmstk/groups.html')
