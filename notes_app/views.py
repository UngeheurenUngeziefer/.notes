from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	"""Home Page"""
	return render(request, 'notes_app/index.html')

def topics(request):
	"""Topics List"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'notes_app/topics.html', context)

def topic(request, topic_id):
	"""Return Topic and all notes"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'notes_app/topic.html', context)

def new_topic(request):
	'''New Topic View'''
	if request.method != 'POST':
		# No Data, create a new form
		form = TopicForm()
	else:
		# POST Data, proceed data
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('notes_app:topics'))

	context = {'form': form}
	return render(request, 'notes_app/new_topic.html', context)

def new_entry(request, topic_id):
	'''Add New Entry to Topic'''
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# No Data, create a new form
		form = EntryForm()
	else:
		# POST Data, proceed data
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('notes_app:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'notes_app/new_entry.html', context)

def edit_entry(request, entry_id):
	'''Edit current note'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('notes_app:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'notes_app/edit_entry.html', context)
