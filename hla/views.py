from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Data, Req
from django.http import JsonResponse

def home(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        qs = Data.objects.filter(
            Q(name__istartswith=term) |
            Q(phuahtu__istartswith=term) |
            Q(satu__istartswith=term)
        ).values_list('name', 'phuahtu', 'satu').distinct()[:10]

        suggestions = []
        for row in qs:
            suggestions.extend([v for v in row if v])
        suggestions = list(set(suggestions))
        return JsonResponse(suggestions, safe=False)

    if request.method == 'POST':
        request_text = request.POST.get('request')
        if request_text:
            Req.objects.create(req=request_text)
        return redirect('home')

    query = request.GET.get('q')
    if query:
        data = Data.objects.filter(
            Q(name__icontains=query) |
            Q(phuahtu__icontains=query) |
            Q(satu__icontains=query)
        )
    else:
        data = Data.objects.all()

    return render(request, 'home.html', {'data': data})


def hla(request, pk):
    data = get_object_or_404(Data, pk=pk)
    return render(request, 'hla.html', {'data': data})
