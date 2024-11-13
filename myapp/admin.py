from django.contrib import admin
from .models import*
# Register your models here.
class rating_user(admin.ModelAdmin):
    readonly_fields = ('rating1','halfrating')

admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Categorie)
admin.site.register(Product,rating_user)
admin.site.register(CartItem)
admin.site.register(checkout)
admin.site.register(order)
admin.site.register(Wishlist)
admin.site.register(Rating)
