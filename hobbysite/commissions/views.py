from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission
# Create your views here.

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissionList.html'
    context_object_name = 'commissions'
    

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission.html'
    context_object_name = 'commission'


def commissionList(request):
    commissions = Commission.objects.all()
    ctx = {
        "commission": commissions
    }
    return render(request, "commissionList.html",ctx)

def commissionDetail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {
        'commission': commission
    }
    return render(request, "commission.html", ctx)


