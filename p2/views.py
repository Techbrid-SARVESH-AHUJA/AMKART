from django.http import HttpResponse
from django.shortcuts import render
from app.models import *
from app.forms import contact_us_form


def index(request):
    Slides=slider.objects.all()
    Categories=categorie.objects.all()
    Details=company.objects.all()
    context={"Slides": Slides, "Categories": Categories, "Details": Details}
    return render(request, "helo/index.html", context)


def contact(request):
    form=contact_us_form
    if request.method=='POST':
        form=contact_us_form(request.POST)
        if form.is_valid:
            form.save()
    Details=company.objects.all()
    context={"Details": Details, "form": form}
    return render(request, 'helo/contact.html', context)


def products(request):
    Mobiles=mobile_phone.objects.all()
    Legos=lego_model.objects.all()
    Bedsheets=bedsheet.objects.all()
    Clocks=clock.objects.all()
    Details=company.objects.all()
    products={"Legos": Legos, "Mobiles": Mobiles, "Bedsheets": Bedsheets, "Clocks": Clocks, "Details": Details}
    return render(request, 'helo/products.html', products)


def cart(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/cart.html', context)


def shipping_rates(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/shipping_rates.html', context)


def login(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/login.html', context)


def signup(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/signup.html', context)


def mobile_phones(request, pk_prod):
    Product=mobile_phone.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/mobile_phones.html', context)


def lego_models(request, pk_prod):
    Product=lego_model.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/lego_models.html', context)


def bedsheets(request, pk_prod):
    Product=bedsheet.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/bedsheets.html', context)


def clocks(request, pk_prod):
    Product=clock.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/clocks.html', context)


def some(request):
    return render(request, 'helo/some.html')
