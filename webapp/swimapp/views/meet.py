'''Meets views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
from hy3parser.hy3parser.line_formats.b_lines import B1Line, B2Line
from hy3parser.hy3parser.line_formats.c_lines import C1Line, C2Line, C3Line
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
        response.write(B1Line(meet).hy3_line)
        response.write('\n' + B2Line(meet).hy3_line)
        response.write('\n' + C1Line(meet.team).hy3_line)
        response.write('\n' + C2Line(meet.team).hy3_line)
        response.write('\n' + C3Line(meet.team).hy3_line)
        for meetevent in meet.meetevent_set.all():
            response.write('\n' + str(meetevent.event))
            for entry in meetevent.entry_set.all():
                response.write('\n' + str(entry))
        return response
