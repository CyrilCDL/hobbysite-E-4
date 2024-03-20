from django.contrib import admin

# Register your models here.

from .models import Commission, Comments

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'peopleRequired', 'created')

class CommentInline(admin.TabularInline):
    model = Comments
    readonly_fields = ('commission', 'created', 'updated')

admin.site.register(Commission,CommissionAdmin)
admin.site.register(Comments)