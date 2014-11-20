'''Meets views for the swimapp'''
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
from hy3parser.hy3parser.line_formats.b_lines import B1Line, B2Line
from hy3parser.hy3parser.line_formats.c_lines import C1Line, C2Line, C3Line
from hy3parser.hy3parser.line_formats.d1_line import D1Line
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
        response = HttpResponse(content_type='text/hyv')
        response['Content-Disposition'] = 'attachment; filename="meet-' \
            + str(meet.id) + '.hyv"'
        response.write('NSW Branch Pointscore - Round 18;11/29/2014;' +
                       '11/29/2014;12/31/2014;L;Lakeside Leisure Centre, ' +
                       'Raymond Terrace;;Hy-Tek Sports Software;5.0Cm;CN;' +
                       '9171W')
        for meetevent in meet.meetevent_set.all():
            response.write('\r\n' + str(meetevent.event.hyv_line))
        return response
