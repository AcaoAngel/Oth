from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


def all_posts(request):
	all_posts = Post.objects.filter(active=True)

	context = {
		'all_posts' : all_posts ,
	}
	return render(request , 'all_posts.html' , context)


def post(request , id):
	#post = Post.objects.get(id=id)
	post = get_object_or_404(Post , id=id)

	context = {
		'post' : post ,
	}
	return render(request , 'detail.html' , context)



def create_post(request):

	# if request.method == 'POST':
	# 	form = PostForm(data=request.POST, files=request.FILES)
	# 	if form.is_valid():
	# 		new_form = form.save(commit=False)
	# 		new_form.user = request.user
	# 		new_form.save()
	# 		# messages.success(request, 'Julkaisu on luotu onnistuneesti')
	# 		return redirect('/allposts')
	# else:
	# 	form = PostForm()

	# context	= {
	# 	'form' : form ,
		
	# }
	# return render(request , 'create.html' , context)


    try:
        current_user = User.objects.get(id=request.user.id)
        if request.user.is_authenticated and current_user.is_staff:
            
            if request.method == 'POST':
            	form = PostForm(data=request.POST, files = request.FILES)
            	if form.is_valid():
            		new_form = form.save(commit=False)
            		print(request.user, type(request.user))
            		new_form.user = request.user
            		new_form.save()
            		messages.success(request, 'Julkaisu on luotu onnistuneesti')
            		return redirect('/allposts')
            form = PostForm()
            return render(request , 'create.html' , {"form": form})
        else:
        	return render(request, "permisions_denied.html" )
    except:
    	return render(request, "permisions_denied.html" )
        


def edit_post(request , id ):
	
    try:
        current_user = User.objects.get(id=request.user.id)
        if request.user.is_authenticated and current_user.is_staff == 1:#permisions to create and edit posts, change to is_superuser for su permisions
            current_user = User.objects.get(id=request.user.id)
            post = get_object_or_404(Post, id=id)
            if request.method == 'GET':
            	form = PostForm(instance = post)#Get the previous form info
            else:
                form = PostForm(request.POST, files = request.FILES, instance=post)
                if form.is_valid():
                    new_form = form.save(commit=False)#when there are fields that must be filled automatically after save we use commit=False
                    new_form.user = request.user
                    new_form.save()
                    return redirect('/allposts')
          
            return render(request , 'edit.html', {'form':form})#we pass as content previous form to fill the fields in the edit post html
        else:
        
            return render(request, "permisions_denied.html")
    except:
    	return render(request, "permisions_denied.html")





