from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
	# home function that takes a POST request
	if request.method == 'POST':
		# form =ListForm
		form = ListForm(request.POST or None)
		
                # if the form is valid then the form is saved, all_items= all of the objects in the list
		if form.is_valid():
			
			#saves the form
			form.save()
			
			# sets all_items to List.objects.all
			all_items = List.objects.all
			
			# message.sucsess takes the POST request and prints "Item Has Been Added To List"
			messages.success(request, ('Item Has Been Added To List!'))
			
			# function returns the render request to home.html with the all_items var
			return render(request, 'home.html', {'all_items': all_items})
		
        # if not POST then set all_items = List.objects.all and return the render request to home.html
	else:
		all_items = List.objects.all
		return render(request, 'home.html', {'all_items': all_items})
	
# Create your views here.
# delete function deltes the to do list items
def delete(request, list_id):
	#gets the item from the list
	item = List.objects.get(pk=list_id)
	#deltes the item
	item.delete()
	#Message that says item has been deleted
	messages.success(request, ('Item Has Been Deleted'))
	#redirects to the home page
	return redirect('home')

# Cross off function sets items.completed to True
def cross_off(request, list_id):
	#gets the item from the list
	item = List.objects.get(pk=list_id)
	#sets that the item has been completed to True
	item.completed = True
	#saves the item as True
	item.save()
	#redirects to the home page
	return redirect('home')

# Uncross function sets items.completed to False
def uncross(request, list_id):
	# sets item to the object you want to get
	item = List.objects.get(pk=list_id)
	# sets the item completed = False
	item.completed = False
	# saves the item
	item.save()
	#redirects to the home page
	return redirect('home')

# edit function allows the user to edit the items in the todo list
def edit(request, list_id):
	
	# if statement for POST request
	if request.method == 'POST':
		# item = object that you want to get
		item = List.objects.get(pk=list_id)
                
		#form= ListForm
		form = ListForm(request.POST or None, instance=item)
                
		# checks if form is valid
		if form.is_valid():
			#saves the form
			form.save()
			#if message.sucsess then print Item has been edited
			messages.success(request, ('Item Has Been Edited!'))
			#redirects to home page
			return redirect('home')
		
	# If not POST request
	else:
		# item = object want to get
		item = List.objects.get(pk=list_id)
		# returns render to edit.html
		return render(request, 'edit.html', {'item': item})
