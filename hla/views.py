from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from .models import Data 
from . models import Req

# This view handles the home page and search functionality
def home(request):

    if request.method == 'POST':
        request_text = request.POST.get('request')
        if request_text:  # Ensure the field is not empty
            req_new = Req(req=request_text)
            req_new.save()
        # You should redirect the user after a successful POST to prevent re-submission
        return redirect('home')
    query = request.GET.get('q')
    print(f"The search query is: '{query}'")

    if query:
        data = Data.objects.filter(
            Q(name__icontains=query) |
            Q(phuahtu__icontains=query) |
            Q(satu__icontains=query)
        )
    else:
        # If no search query, show all songs
        data = Data.objects.all()
       
    return render(request, 'home.html', {'data': data})

# This view handles the detail page for a single song
def hla(request, pk):
    # Use get_object_or_404 to fetch the song or return a 404 error
    data = get_object_or_404(Data, pk=pk)
    
    # Pass the single song object to the new 'hla.html' template
    return render(request, 'hla.html', {'data': data})