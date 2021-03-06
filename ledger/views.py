from django.shortcuts import render_to_response
from ledger.models import Ledger


def home(request):
    # lists ledgers in reverse order
    args = {}
    ledgers = Ledger.objects.all()
    args['ledgers'] = ledgers.order_by('content', 'id').reverse()
    args['ledger'] = args['ledgers'].first()

    return render_to_response('ledger/ledger_base.html', args)


def view_ledger(request, ledger_id=1):
    args = {}
    args['ledger'] = Ledger.objects.get(id=ledger_id)
    args['ledgers'] = Ledger.objects.all()
    return render_to_response('ledger/ledger.html', args)
