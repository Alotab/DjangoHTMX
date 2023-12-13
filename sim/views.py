# views.py in sim
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Person
from django.shortcuts import get_object_or_404
from .forms import UpdatePerson


def search_view(request):
    all_people = Person.objects.all()
    context = {'count': all_people.count()}
    return render(request, 'sim/search.html', context)


def search_results_view(request):
    query = request.GET.get('search', '')
    print(f'{query = }')

    all_people = Person.objects.all()
    if query:
        people = all_people.filter(name__icontains=query)
    else:
        people = []

    context = {'people': people, 'count': all_people.count()}
    return render(request, 'sim/search_results.html', context)


def updatePerson(request, pk):
    lead = get_object_or_404(Person, pk=pk)
    lead_id = lead.id
    
    if request.method == 'POST':
        form = UpdatePerson(request.POST, instance=lead)
        # form = Leadform()
        if form.is_valid():
            form.save()
            return redirect('search_view')
    else:
        form = UpdatePerson(instance=lead)
    return render(request, 'sim/search.html', {'form': form, 'lead_id': lead_id })