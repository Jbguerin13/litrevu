from django.contrib import admin

from review.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

admin.site.register(Ticket, TicketAdmin)

#autre technique via decorateur @admin.register(VPN)

# class VPNAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
#     search_fields = ["ip_begin", "ip_end", "name"]
#     list_filter = ["is_default"]
#     list_display = (
#         "name",
#         "ip_begin",
#         "ip_end",
#         "mask",
#         "is_default",
#     )
