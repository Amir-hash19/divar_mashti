from django.contrib import admin
from .models import Product, Category, Order, OrderItem



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("brand", "title", "status", "date_created")
    list_filter = ("date_created", "updated_at", "status")
    search_fields = ("status", "date_created")
    readonly_fields = ("updated_at", )
    list_display_links = ("title", )
    list_editable = ("status", )
    save_as_continue = True
    save_on_top = True
    sortable_by = ("title", "date_created")
    show_full_result_count = True


    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("brand", "title", "status")
        return ("title", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("status", "created_at", "total_price")
    list_filter = ("created_at", "status", "shipped_at")
    search_fields = ("customer__fullname", )
    readonly_fields = ("shipped_at", "delivered_at")
    save_as_continue = True
    save_on_top = True



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", )


    