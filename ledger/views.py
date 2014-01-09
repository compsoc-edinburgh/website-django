from django.shortcuts import render
from django.shortcuts import render_to_response
from ledger.models import Ledger

# Create your views here.
def home(request):
    # lists ledgers in reverse order
    args = {}
    args['ledgers']= Ledger.objects.all()

    return render_to_response('ledger_base.html', args)
