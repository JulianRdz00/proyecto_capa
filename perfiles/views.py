from datetime import timezone
from django.shortcuts import render
from .forms import Perfiles
from .forms import FormPerfiles
from django.shortcuts import redirect


def index(request):
    return render(request, 'perfiles/index.html')

def perfil_edit(request):
    if request.method == "EDIT":
        form = FormPerfiles(request.EDIT)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.published_date = timezone.now()
            edit.save()
            return redirect('base.html', pk=edit.pk)
    else:
        form = FormPerfiles()        
    return render(request, 'perfiles/perfil_edit.html', {'form': form})