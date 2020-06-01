from django.contrib import admin
from girafic_app.models import Catalog, Box, Dreamcatcher, Letter, Review, ClientData, BoxOrder, DreamcatcherOrder, LetterOrder, Order

# Register your models here.
admin.site.register(Catalog)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'data')

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'catalog', 'description', 'lenght', 'width', 'height', 'cost')

@admin.register(Dreamcatcher)
class DreamcatcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'catalog', 'description', 'diameter', 'cost')

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'catalog', 'description', 'lenght', 'width', 'color', 'cost')

class ClientDataInline(admin.TabularInline):
    model = ClientData

class BoxOrderInline(admin.TabularInline):
    model = BoxOrder

class DreamcatcherOrderInline(admin.TabularInline):
    model = DreamcatcherOrder

class LetterOrderInline(admin.TabularInline):
    model = LetterOrder

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ClientDataInline, BoxOrderInline, DreamcatcherOrderInline, LetterOrderInline
    ]
