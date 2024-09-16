from django.contrib import admin
from .models import Product, Profile, Review, Category

# Inline to display Reviews within Product
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

# Product Admin Configuration
class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]  # Inline for Reviews
    list_display = ('name', 'description', 'profile')  # Display name, description, and profile
    filter_horizontal = ('categories',)  # Use filter widget for categories

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Category)
