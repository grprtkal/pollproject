from django.contrib import admin
from polls.models import Choice, Poll 

class ChoiceInline(admin.TabularInline): # you can also have the choice stacked by using (admin.StackedInLine)
	model = Choice #choice objects are dited on the Poll admin page 
	extra = 3 #number of choices by default when you add a poll 

class PollAdmin(admin.ModelAdmin): 
	fieldsets = [
		(None, {'fields': ['question']}), 
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), #the first element of each tuple is the title of the fieldset (i.e date information)
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently') #list_display is a tuple of field names 
	list_filter = ['pub_date'] #add a filter sidebar that lets people filter the change list by date published
	search_fields = ['question'] #add a search field on top of your questions 

admin.site.register(Poll, PollAdmin)


# Register your models here.
