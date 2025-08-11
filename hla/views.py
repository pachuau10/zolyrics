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




def hla(request, name):
    # Find by 'name' field in your model
    data = get_object_or_404(Data, name=name)

    # Unique view tracking per session
    viewed_posts = request.session.get('viewed_posts', [])
    if name not in viewed_posts:
        data.views += 1
        data.save(update_fields=['views'])
        viewed_posts.append(name)
        request.session['viewed_posts'] = viewed_posts

    return render(request, 'hla.html', {'data': data})





def request_view(request):
    return render(request,'request.html')


def get_client_ip(request):
    """Get IP address from request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip