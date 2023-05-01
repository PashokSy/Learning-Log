from django.shortcuts import render

from learning_logs.models import Topic


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


# TODO fix topics list is empty
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topic': topics}
    return render(request, 'learning_logs/topics.html', context)
