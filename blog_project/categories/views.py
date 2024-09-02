from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method =='POST': #user post request kortece
        category_form= forms.CategoryForm(request.POST) # user er post request data ekhane capture korteci
        if category_form.is_valid(): #post kora data gula valid kina dekhteci
            category_form.save() #jodi valid hoy tahole database e save korbo
            return redirect('add_category') #sob thik thakle take add_category ei url e pathai dibo
    else:
        category_form= forms.CategoryForm() #user normally web site e gele blank form pabe
    return render(request,'add_category.html', {'form' : category_form})