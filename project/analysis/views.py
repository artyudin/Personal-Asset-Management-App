from django.shortcuts import render, redirect
from django.views.generic import View
from .analysis_models import Client, Risk, Investment_policy
from users.models import Profile
from .analysis_forms import ClientForm, RiskForm, Investment_policyForm 
from securities.securities_models import Bond
from django.http import JsonResponse
from analysis.utilities.risk_calc import RiskAnalysis,  Analysis_portfolio, ModelPortfolio
# from analysis.utilities.model_portfolio import ModelPortfolio
from portfolio.models import Portfolio, Asset
from django.contrib.contenttypes.models import ContentType
from .reporting_policy import report
from django.contrib.auth.models import User



class ClientCreateView(View):
    template_name = 'dashboard.html'
    model = Client
    form_class = ClientForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            client = form.save(commit = False)
            client.user = request.user
            client.save()
            # i = Investment_policyView(View)
            # context = i.get_context(Investment_policyForm())
            # return render(request, self.template_name, context)
            return redirect('/analysis/policy')
            # return JsonResponse("saved")
        else:
            print(form.errors)
            context = dict(form=form,submit_text='Create')
            return render(request, self.template_name, context)

    def get_context(self, form):
        return {
            "client_form": form,
            "action": "analysis:analysis",
            "method": "POST",
            "submit_text": "Create Risk Profile"
        }


class RiskView(View):
    template_name = 'dashboard.html'
    model = Risk
    form_class = RiskForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form, request.GET.get('next',''))
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid():
            risk = form.save(commit = False)
            score = int(data.get('cash_reserves')[0]) + int(data.get('time_horizont')[0])
            score += int(data.get('market_loss')[0]) + int(data.get('investment_experience')[0]) 
            score += int(data.get('investment_return')[0])
            # recommendation = ModelPortfolio(score).get_recommendation()
            risk.user = request.user
            risk.score = score
            risk.save()
            if request.GET.get('next'):
                redirect(request.GET.get('next'))
            return render(request, self.template_name)
        else:
            context = dict(form=form,submit_text='Create')

            return render(request, self.template_name, context)

    def get_context(self, form, next_=''):
        return {
            "risk_form": form,
            "action": "analysis:risk",
            "DOUBLE_BONUS": '?next='+ next_,
            "method": "POST",
            "submit_text": "Submit Risk Form"
        }

class Investment_policyView(View):
    template_name = 'dashboard.html'
    model = Investment_policy
    form_class = Investment_policyForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            investment_policy = form.save(commit = False)
            investment_policy.user = request.user 
            investment_policy.save()
            return render(request, self.template_name)
        # What do you want to do with this
        print(form.errors)
        return JsonResponse({'result': 'failed'})

    def get_context(self, form):
        return {
            "investment_form": form,
            "action": "analysis:policy",
            "method": "POST",
            "submit_text": "Submit Policy Form"
        }


class BetaAnalysisView(View):
    model = Portfolio
    template_name = 'analysis/analysis.html'

    def get(self,request,id):
        analysis = Analysis_portfolio()
        context = analysis.anlaysis_portfolio(id)
        return render(request, self.template_name, context) 

class ReportInvestmentPolicy(View):
    def get(self,request):

        
        return report(request)
        # Create the HttpResponse object with the appropriate PDF headers.
        
class Compare_with_model(View): 
    template_name = "analysis/compare.html"

    def get(self,request,id):

        if not hasattr(request.user,'risk'):
            return redirect('/analysis/risk?next=/analysis/compare/{}'.format(id))
        portfolio = Portfolio.objects.get(id=id)
        print(id)
        print(portfolio.user.id)
        model = ModelPortfolio()
        model_id = model.recommended_portfolio(request,portfolio.user)
        id_model = model_id
        print(id)
        print(id_model)
        analysis = Analysis_portfolio()
        context1 = analysis.anlaysis_portfolio(id)
        context2 = analysis.anlaysis_portfolio(id_model)
        context = dict(owen = context1, model = context2)
        print(context)
        return render(request, self.template_name, context) 

class View_model_portfolio(View):
    template_name = "read.html"


    def get(self,request):
        
        if not hasattr(request.user,'risk'):
            return redirect('/analysis/risk?next=/analysis/compare/{}'.format(id))
        model = ModelPortfolio()
        # user = User.objects.get(id= request.user)
        model_id = model.recommended_portfolio(request,request.user)
        portfolio = Portfolio.objects.get(id=model_id)
        # assets = Asset.objects.filter(portfolio=portfolio)
        assets= Asset.objects.raw('''SELECT *, cost_basis * quantity as value 
            FROM portfolio_asset
            WHERE portfolio_asset.portfolio_id = %s ''',(id,))
        # print(assets)
        portfolio_value = 0 
        for asset in assets:
            portfolio_value += asset.value
        
        assets = [ asset.to_json(asset.value,portfolio_value)for asset in assets ]
        for asset in assets:
            asset_value = round(asset_value,2)

        # print(assets)
        return JsonResponse({'asset':assets,'portfolio_value':portfolio_value})







# class Risk_calculationsView(View):
#     template_name = 'analysis/risk_analysis.html'




# class Profit_loss(View):
#     template_name = 'analysis/p_l.html'
#     model = Portfolio
#     context = None

#     def post(self, request):
#         form = self.form_class(data=request.POST)
#         data=request.POST
#         result = data
#         return JsonResponse({'result': result})

#        


















