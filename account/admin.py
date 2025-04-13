from django.contrib import admin
from .models import UserAccount

       

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "date_created")
    list_filter = ("is_superuser", "date_created")
    search_fields = ("date_created", "fullname")
  

  
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("fullname", "email")
        return ("email", )
