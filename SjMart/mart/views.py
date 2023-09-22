from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Acquisition,name,staff,job_categories,shifts,staff_in_shift,suppliers

def home(request):
    return render(request,"mart/home.html")

def goods(request):
    stock  = Acquisition.objects.all()
    context = {
        "objects":stock,
    }
    return render(request,"mart/goods.html",context)

def purchase(request):
    if request.method =='POST':
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        qnty = request.POST.get('quantity')
        price = request.POST.get('price')
        dealer = request.POST.get('dealer')
        # contact = request.POST.get('contact')
        # getting the category name
        name_obj = name.objects.get(name=category)

        Acquisition.objects.create(brand = brand,price=price,quantity=qnty,distr=dealer,name=name_obj)
        return redirect('mart:goods')

    data = name.objects.all()
    distributer = suppliers.objects.all()
    context = {
        "data":data,
        "distr":distributer
    }
    return render(request,"mart/purchase.html",context)

def buy(request,brand_id):
    if request.method == 'POST':
        x=Acquisition.objects.get(pk = brand_id)
        order = request.POST.get('quantity')
        x.quantity +=int(order)
        x.save()
        return redirect("mart:goods")

        
    name = get_object_or_404(Acquisition,pk = brand_id)
    context = {
        "brand":name,
    }

    return render(request,'mart/buy.html',context)

def sales(request):
    stock  = Acquisition.objects.all()
    context = {
        "objects":stock,
    }

    if request.method=='POST':
        brand_name = request.POST.get('brand')
        qty = request.POST.get('quantity')
        try:
            brand_db = Acquisition.objects.get(brand=brand_name)
            if brand_db.quantity >= int(qty):
                brand_db.quantity -= int(qty)
                brand_db.save()
                return render(request,"mart/sales.html")
            else:
                return HttpResponse(f'Insufficient quantity for {brand_name}')
        except Acquisition.DoesNotExist:
            return HttpResponse(f'Brand not available: {brand_name}')
        
    

    return render(request,"mart/sales.html",context)

def store_suppliers(request):
    return render(request,'mart/suppliers.html')

def view_staff(request):
     # Get the job category object with the name 'corporate'
    corporate_category = job_categories.objects.get(cat_name='corporate')
    accountant_cat = job_categories.objects.get(cat_name = 'accountant')
    janitor_cat = job_categories.objects.get(cat_name = 'janitors')
    quality_cat = job_categories.objects.get(cat_name = 'Quality assurance')

    # Filter staff members by the corporate job category ID
    corporate_staff = staff.objects.filter(job_cat=corporate_category)
    accountant = staff.objects.filter(job_cat=accountant_cat)
    janitor = staff.objects.filter(job_cat=janitor_cat)
    quality = staff.objects.filter(job_cat=quality_cat)

    # You can also retrieve all staff members for other purposes
    all_staff = staff.objects.all()

    context = {
        "staff": all_staff,
        "corporate": corporate_staff,
        "accountant":accountant,
        "janitor":janitor,
        "quality":quality,
    }
    return render(request, 'mart/staff.html', context)

def staff_shifts(request):
    # early shift
    early_shift = shifts.objects.get(period='6am-12pm')
    early_staff = staff_in_shift.objects.filter(shift=early_shift)
    # mid shift
    mid_shift = shifts.objects.get(period='12pm-6pm')
    mid_staff = staff_in_shift.objects.filter(shift=mid_shift)
    # late shift
    late_shift = shifts.objects.get(period='6pm-11pm')
    late_staff = staff_in_shift.objects.filter(shift=late_shift)
    context = {
        "early":early_staff,
        "mid":mid_staff,
        "late":late_staff
    }
    return render(request,'mart/shifts.html',context)

def model(request):
    return render(request,"mart/model.html")
# Create your views here.
