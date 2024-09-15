from django.shortcuts import render, get_object_or_404
from .models import Products, ProductImage  # Importing both models
from django.core.paginator import Paginator

# View to list all products with pagination
def shop(request):
    products_list = Products.objects.all()  # Fetch all products
    products_list_count = Products.objects.all().count()  # Fetch all products

    # Set the number of products per page
    paginator = Paginator(products_list, 8)  # Show 8 products per page

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the products for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the page_obj to the context
    context = {'page_obj': page_obj,"products_list_count":products_list_count}
    return render(request, 'allshop.html', context)


def product_details(request, pk):
    product = get_object_or_404(Products, id=pk)  # Fetch product by primary key
    images = ProductImage.objects.filter(product=product)  # Fetch all images associated with the product
    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'product_list.html', context)



def shop_category(request,pk):
    products_list = Products.objects.filter(category=pk)  # Fetch all products
    products_list_count = Products.objects.filter(category=pk).count()  # Fetch all products

    # Set the number of products per page
    paginator = Paginator(products_list, 8)  # Show 8 products per page

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the products for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the page_obj to the context
    context = {'page_obj': page_obj,"products_list_count":products_list_count}
    return render(request, 'allshop_category.html', context)
