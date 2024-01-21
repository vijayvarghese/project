from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyFormData

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        print("form data", form) 
        if form.is_valid():
            form.save()
            print("Form saved successfully!")
            return redirect('home')  # Redirect to the same page after successful form submission
        else:
            print("Form is not valid!")
            print("Form errors:", form.errors)
    else:
        form = MyForm()

    existing_data = MyFormData.objects.all()
    print("Existing data:", existing_data)
    return render(request, 'template.html', {'form': form, 'existing_data': existing_data})
