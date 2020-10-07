from django.shortcuts import render
from .models import Topic

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