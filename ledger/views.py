from django.shortcuts import render
from django.shortcuts import render_to_response
from ledger.models import Ledger
from compsoc.models import Page, Event

# Create your views here.
def home(request):
    # lists ledgers in reverse order
    args = {}
    args['ledgers']= Ledger.objects.all()

    return render_to_response('ledger/ledger_base.html', args)

def view_ledger(request, ledger_id=1):
    args = {}
    args['ledger'] = Ledger.objects.get(id=ledger_id)
    return render_to_response('ledger/ledger.html', args)
