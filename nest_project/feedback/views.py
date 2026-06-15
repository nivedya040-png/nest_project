from django.shortcuts import render, redirect
from .forms import feedbackform

def home(request):
    return render(request, 'home.html')

def submit_feedback(request):
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = feedbackform()

    return render(request, 'feedback_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

# Create your views here.
