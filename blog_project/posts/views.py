from django.shortcuts import render, redirect
from . import forms
from. import models
# Create your views here.
def add_post(request):
    if request.method =='POST': #user post request kortece
        post_form= forms.PostForm(request.POST) # user er post request data ekhane capture korteci
        if post_form.is_valid(): #post kora data gula valid kina dekhteci
            post_form.save() #jodi valid hoy tahole database e save korbo
            return redirect('add_post') #sob thik thakle take add_category ei url e pathai dibo
    else:
        post_form= forms.PostForm() #user normally web site e gele blank form pabe
    return render(request,'add_post.html', {'form' : post_form})



# Edit
def edit_post(request, id):
    post= models.Post.objects.get(pk=id)
    post_form= forms.PostForm(instance=post)
    # print(post.title)
    if request.method =='POST': #user post request kortece
        post_form= forms.PostForm(request.POST, instance= post) # user er post request data ekhane capture korteci
        if post_form.is_valid(): #post kora data gula valid kina dekhteci
            post_form.save() #jodi valid hoy tahole database e save korbo
            return redirect('homepage') #sob thik thakle take add_category ei url e pathai dibo
        
    return render(request,'add_post.html', {'form' : post_form})


def delete_post(request, id):
    post= models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
