
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from salaire.models import Contract, Cost, Pricing,  Month, Day, Summary, ContractEnd
from salaire.forms import ContractForm, CostForm,  PricingForm, MonthForm, DayForm, SummaryForm, ContractEndForm
import calendar, locale
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

## login page
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'salaire/login.html', {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'salaire/login.html')

## logout page
def custom_logout(request):
    logout(request)
    #message = "logout"
    #return HttpResponse(message)
    return render(request,'salaire/logout.html')

## home
@login_required
def home(request):
    return render(
        request,
        "salaire/home.html"
    )

# blanck page
@login_required
def delete(request):
    message = ""
    return HttpResponse(message)

# restricted_access
@login_required
def restricted_access(request):
    return render(
        request,
        "salaire/restricted_access.html",
    )

## cost

# list
@login_required
@permission_required('salaire.view_cost',login_url='restricted_access')
def cost_list(request):
    obj= Cost.objects.all()
    return render(
        request,
        "salaire/cost/list.html",
        {"obj":obj}
    )

# detail
@login_required
@permission_required('salaire.view_cost',login_url='restricted_access')
def cost_detail(request,id):
    obj = Cost.objects.get(id=id)
    return render(request,
        'salaire/cost/detail.html',
        {"obj":obj}
    )

# create
@login_required
@permission_required('salaire.add_cost',login_url='restricted_access')
def cost_create(request):
    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('cost_detail', obj.id)
    else:
        form = CostForm()
    return render(
        request,
        "salaire/cost/create.html",
        {"obj" : form}
    )

# update
@login_required
@permission_required('salaire.change_cost',login_url='restricted_access')
def cost_update(request,id):
    obj = Cost.objects.get(id=id)
    months=obj.month_set.all()
    linked_months=months.exists()
    months='<br>'.join(map(str,months))
    summaries=obj.summary_set.all()
    linked_summaries=summaries.exists()
    summaries='<br>'.join(map(str,summaries))
    if request.method == 'POST':
        form = CostForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
            return redirect('cost_detail', obj.id)
    else:
        form = CostForm(instance=obj)
    context = {
        "linked_months":linked_months,
        "months":months,
        "linked_summaries":linked_summaries,
        "summaries":summaries,
        "obj":form,
    }
    return render(
        request,
        'salaire/cost/update.html',
         context
    )

# delete
@login_required
@permission_required('salaire.delete_cost',login_url='restricted_access')
def cost_delete(request, id):
    obj = Cost.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/cost/delete.html',
        {'obj': obj})

## pricing

# list
@login_required
@permission_required('salaire.view_pricing',login_url='restricted_access')
def pricing_list(request):
    obj= Pricing.objects.all()
    return render(
        request,
        "salaire/pricing/list.html",
        {"obj":obj}
    )

# detail
@login_required
@permission_required('salaire.view_pricing',login_url='restricted_access')
def pricing_detail(request,id):
    obj = Pricing.objects.get(id=id)
    return render(request,
        'salaire/pricing/detail.html',
        {"obj":obj}
    )

# create
@login_required
@permission_required('salaire.add_pricing',login_url='restricted_access')
def pricing_create(request):
    if request.method == 'POST':
        form = PricingForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('pricing_detail', obj.id)
    else:
        form = PricingForm()
    return render(
        request,
        "salaire/pricing/create.html",
        {'obj' : form}
    )

# update
@login_required
@permission_required('salaire.change_pricing',login_url='restricted_access')
def pricing_update(request,id):
    obj = Pricing.objects.get(id=id)
    contracts=obj.contract_set.all()
    linked=contracts.exists()
    contracts=contracts.values_list("name",flat=True)
    contracts='<br>'.join(map(str,contracts))
    if request.method == 'POST':
        form = PricingForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
            return redirect('pricing_detail', obj.id)
    else:
        form = PricingForm(instance=obj)
    context = {
        "linked":linked,
        "contracts":contracts,
        "obj":form,
    }
    return render(request,
        'salaire/pricing/update.html',
        context
    )

# delete
@login_required
@permission_required('salaire.delete_pricing',login_url='restricted_access')
def pricing_delete(request, id):
    obj = Pricing.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/pricing/delete.html',
        {'obj': obj})

## contracts

# list
@login_required
@permission_required('salaire.view_contract',login_url='restricted_access')
def contract_list(request):
    obj= Contract.objects.all()
    return render(
        request,
        "salaire/contract/list.html",
        {"obj":obj}
    )

# detail
@login_required
@permission_required('salaire.view_contract',login_url='restricted_access')
def contract_detail(request,id):
    obj = Contract.objects.get(id=id)
    return render(request,
        'salaire/contract/detail.html',
        {"obj":obj}
    )

# create
@login_required
@permission_required('salaire.add_contract',login_url='restricted_access')
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('contract_detail', obj.id)
    else:
        form = ContractForm()
    return render(
        request,
        "salaire/contract/create.html",
        {'obj' : form}
    )

# update
@login_required
@permission_required('salaire.change_contract',login_url='restricted_access')
def contract_update(request,id):
    obj = Contract.objects.get(id=id)
    months=obj.month_set.all()
    linked=months.exists()
    months='<br>'.join(map(str,months))
    if request.method == 'POST':
        form = ContractForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
            return redirect('pricing_detail', obj.id)
    else:
        form = ContractForm(instance=obj)

    context = {
        "linked":linked,
        "months":months,
        "obj":form,
    }
    return render(request,
        'salaire/contract/update.html',
        context
    )

# delete
@login_required
@permission_required('salaire.delete_contract',login_url='restricted_access')
def contract_delete(request, id):
    obj = Contract.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/contract/delete.html',
        {'obj': obj}
    )

## month

# list
@login_required
@permission_required('salaire.view_month',login_url='restricted_access')
def month_list(request):
    obj= Contract.objects.all()
    return render(
        request,
        "salaire/month/list.html",
        {"obj":obj}
    )

# contract months
@login_required
@permission_required('salaire.view_month',login_url='restricted_access')
def month_list_contract(request,id):
    contract=Contract.objects.get(id=id)
    obj= Month.objects.all().filter(name=id)
    context = {
        "contract":contract,
        "obj":obj,
    }
    return render(
        request,
        "salaire/month/list_contract.html",
        context
    )

# detail
@login_required
@permission_required('salaire.view_month',login_url='restricted_access')
def month_detail(request,id):
    obj = Month.objects.get(id=id)
    days = Day.objects.filter(name=obj)
    contract = Contract.objects.get(name=obj.name)
    cost= Cost.objects.get(name=obj.cost)
    pricing=Pricing.objects.get(name=contract.pricing)
    context = {
        "contract":contract,
        "days": days,
        "obj":obj,
        "cost":cost,
        "pricing":pricing
    }
    return render(
        request,
        'salaire/month/detail.html',
        context
    )

# create
@login_required
@permission_required('salaire.add_month',login_url='restricted_access')
def month_create(request):
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    if request.method == 'POST':
        form = MonthForm(request.POST)
        if form.is_valid():
            obj=form.save()
            cal = calendar.monthcalendar(obj.year,obj.month)
            obj.month_name = timezone.datetime(obj.year, obj.month,1).strftime("%B")
            obj.save()
            for week in cal:
                for day in week:
                    if day!=0:
                        days = Day.objects.create(
                            name = obj,
                            day_name = timezone.datetime(obj.year, obj.month, day).strftime("%A"),
                            day = day,
                        )
                        days.save()
            return redirect('day_update',id=obj.id)

    else:
        form = MonthForm()
    return render(
        request,
        "salaire/month/create.html",
        {'obj' : form}
    )

# update
@login_required
@permission_required('salaire.change_day',login_url='restricted_access')
def day_update(request,id):
    month = Month.objects.get(id=id)
    contract=Contract.objects.get(name=month.name)
    days = Day.objects.filter(name=month)
    days.filter(day_name="lundi").update(ie=contract.monday_ie,meal=contract.monday_meal,snack=contract.monday_snack)
    days.filter(day_name="mardi").update(ie=contract.tuesday_ie,meal=contract.tuesday_meal,snack=contract.tuesday_snack)
    days.filter(day_name="mercredi").update(ie=contract.wednesday_ie,meal=contract.wednesday_meal,snack=contract.wednesday_snack)
    days.filter(day_name="jeudi").update(ie=contract.thursday_ie,meal=contract.thursday_meal,snack=contract.thursday_snack)
    days.filter(day_name="vendredi").update(ie=contract.friday_ie,meal=contract.friday_meal,snack=contract.friday_snack)
    days.filter(day_name="samedi").update(ie=contract.saturday_ie,meal=contract.saturday_meal,snack=contract.saturday_snack)
    days.filter(day_name="dimanche").update(ie=contract.sunday_ie,meal=contract.sunday_meal,snack=contract.sunday_snack)
    DayFormSet = forms.modelformset_factory(Day, form=DayForm,extra=0)
    if request.method == 'POST':
        formset = DayFormSet(request.POST,queryset=days)
        if formset.is_valid():
            formset.save()
            month.compute()
            return redirect('delete')
    else:
        formset = DayFormSet(queryset=days)
    context = {
        "month":month,
        "formset":formset,
    }
    return render(
        request,
        'salaire/month/day_update.html',
        context
    )

# update
@login_required
@permission_required('salaire.change_month',login_url='restricted_access')
def month_update(request,id):
    obj = Month.objects.get(id=id)
    if request.method == 'POST':
        form = MonthForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('day_update',obj.id)
    else:
        form = MonthForm(instance=obj)
    return render(request,
            'salaire/month/update.html',
            {'obj': form})

# delete
@login_required
@permission_required('salaire.delete_month',login_url='restricted_access')
def month_delete(request, id):
    obj = Month.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/month/delete.html',
        {'obj': obj})

## summary

# list
@login_required
@permission_required('salaire.view_summary',login_url='restricted_access')
def summary_list(request):
    obj= Summary.objects.all()
    return render(
        request,
        "salaire/summary/list.html",
        {"obj":obj}
    )

# detail
@login_required
@permission_required('salaire.view_summary',login_url='restricted_access')
def summary_detail(request,id):
    obj = Summary.objects.get(id=id)
    month = Month.objects.filter(month=obj.month,year=obj.year)
    context = {
        "obj":obj,
        "month":month,
    }
    return render(
        request,
        'salaire/summary/detail.html',
        context
    )

# create
@login_required
@permission_required('salaire.add_summary',login_url='restricted_access')
def summary_create(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('summary_detail', obj.id)
    else:
        form = SummaryForm()
    return render(
        request,
        "salaire/summary/create.html",
        {'obj' : form}
    )

# update
@login_required
@permission_required('salaire.change_summary',login_url='restricted_access')
def summary_update(request,id):
    obj = Summary.objects.get(id=id)
    if request.method == 'POST':
        form = SummaryForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
            return redirect('summary_detail', obj.id)
    else:
        form = SummaryForm(instance=obj)
    return render(
        request,
        'salaire/summary/update.html',
        {'obj': form}
    )

# delete
@login_required
@permission_required('salaire.delete_summary',login_url='restricted_access')
def summary_delete(request, id):
    obj = Summary.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/summary/delete.html',
        {'obj': obj})

## Contract end

# list
@login_required
@permission_required('salaire.view_contractend',login_url='restricted_access')
def contractend_list(request):
    obj= ContractEnd.objects.all()
    return render(
        request,
        "salaire/contractend/list.html",
        {"obj":obj}
    )

# detail
@login_required
@permission_required('salaire.view_contractend',login_url='restricted_access')
def contractend_detail(request,id):
    obj = ContractEnd.objects.get(id=id)
    return render(
        request,
        'salaire/contractend/detail.html',
         {"obj":obj}
    )

# create
@login_required
@permission_required('salaire.add_contractend',login_url='restricted_access')
def contractend_create(request):
    if request.method == 'POST':
        form = ContractEndForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('contractend_detail', obj.id)
    else:
        form = ContractEndForm()
    return render(
        request,
        "salaire/contractend/create.html",
        {'obj' : form}
    )

# update
@login_required
@permission_required('salaire.change_contractend',login_url='restricted_access')
def contractend_update(request,id):
    obj = ContractEnd.objects.get(id=id)
    if request.method == 'POST':
        form = ContractEndForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
            return redirect('contractend_detail', obj.id)
    else:
        form = ContractEndForm(instance=obj)
    return render(
        request,
        'salaire/contractend/update.html',
        {'obj': form}
    )

# delete
@login_required
@permission_required('salaire.delete_contractend',login_url='restricted_access')
def contractend_delete(request, id):
    obj = ContractEnd.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('delete')
    return render(request,
        'salaire/contractend/delete.html',
        {'obj': obj})