from django.contrib import admin
from .models import Data, Req, ViewTracker

# Create a custom ModelAdmin for the Data model
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    # This tuple specifies which fields to display in the list view of the admin.
    # It makes the list page more informative and easier to browse.
    list_display = ('name', 'phuahtu', 'satu')

    # This tuple adds a search box to the admin page.
    # The search functionality will query these fields, making it easy to find specific entries.
    search_fields = ('name', 'phuahtu', 'satu')

    # This adds a right-hand sidebar to filter the change list page.
    # We'll filter by the 'phuahtu' and 'satu' fields.
    list_filter = ('phuahtu', 'satu')


# Create a custom ModelAdmin for the Req model
@admin.register(Req)
class ReqAdmin(admin.ModelAdmin):
    # This will display the full text of the request in the admin list view.
    list_display = ('req',)
    
    # This adds a search box to the admin page that searches the 'req' field.
    search_fields = ('req',)

