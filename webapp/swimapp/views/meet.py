'''Meets views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
from swimapp.models.meet import Meet


class MeetListView(ListView):
    '''meets view'''
    model = Meet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MeetListView, self).dispatch(*args, **kwargs)


class MeetHy3File(View):
    '''download hy3file'''
    def get(self, request, *args, **kwargs):
        meet = Meet.objects.get(id=self.kwargs['pk'])
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="meet-' \
            + str(meet.id) + '.txt"'
        response.write('test')
        return response
