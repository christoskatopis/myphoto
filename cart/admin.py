
from django.contrib import admin
from .models import Order

class OrderAdmin (admin.ModelAdmin):
  list_display = ["user","date_created","amount","is_completed"]
  list_display_links=["user"]
  search_fields=["user","amount"]
  list_editable=["is_completed"]

  def has_add_permission(self, request, obj=None):
     return False

 
     
  class Meta:
  	model = Order

admin.site.register(Order,OrderAdmin)