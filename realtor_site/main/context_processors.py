from .forms import ApplicationForm

def application_form(request):
    return {
        'form': ApplicationForm()
    } 