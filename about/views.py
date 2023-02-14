from django.shortcuts import render

def recyclables(request):
    return render(request, 'about/recyclables.html')
def FAQ(request):
    return render(request, 'about/FAQ.html')

