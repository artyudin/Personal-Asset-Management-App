from django.shortcuts import render, redirect
from portfolio.models import Portfolio, Asset
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from portfolio.forms import PortfolioForm, AssetForm
from securities.securities_forms import (
    StockForm, BondForm, ExchangeTradedFundForm
)
from django.http import JsonResponse
from django.views.generic import DetailView
    



class Index(LoginRequiredMixin,View):
    template_name = "dashboard.html"

    def get(self, request): 
        return render(request, self.template_name,{'portfolio_view':  True} ) 

class CreatePortfolio(LoginRequiredMixin,View):
    template_name = "portfolio/portfolio_form.html"
    form_class = PortfolioForm
    success_url = "portfolio:create"
    context = None

    def get(self,request):
        form = self.form_class()
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self,request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid(): 
            portfolio = Portfolio.objects.create(
                user = request.user,
                portfolio_name=data.get('portfolio_name')
                )
            
            return redirect('portfolio:show_list')
        
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)


        
    def get_context(self, form):
        return {
            "form": form,
            "action": "portfolio:create",
            "method": "POST",
            "submit_text": "Add new Portfolio"
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class ShowPortfolio(LoginRequiredMixin,View):
    
    def get(self,request):
        portfolios = Portfolio.objects.filter(user=request.user)
        if request.is_ajax():
            portfolios = [portfolio.to_json() for portfolio in portfolios]
            return JsonResponse({'portfolios':portfolios})


        return render(request, 'dashboard.html',
         {'portfolio_view':True}
         )

    def post(self,request):
        return HttpResponseNotAllowed(['GET'])


class DeletePortfolio(LoginRequiredMixin,View):
    success_url="portfolio:show_list"
    
    def get(self,request,id):
        portfolio_object = Portfolio.objects.get(id=id,
            user=request.user).delete()
        return redirect(self.success_url)
       

    def post(self,request):
        return HttpResponseNotAllowed(['GET'])


class UpdatePortfolio(View):
    def get(self,request,id):
        portfolio_object = Portfolio.objects.get(id=id)
        return JsonResponse({'portfolio':portfolio_object.to_json()})

    def post(self,request, id):
        data = request.POST
        print(data)
        if not data.get('portfolio_name'):
            return JsonResponse({'status':'failure', 'message':'invalid portfolio name'})
        portfolio_name = data.get('portfolio_name')
        portfolio_object = Portfolio.objects.get(id=id,
            user=request.user)
        portfolio_object.portfolio_name = portfolio_name
        portfolio_object.save()
        return JsonResponse({'portfolio':portfolio_object.to_json()})



class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/read.html'

    def get_context_data(self,**kwargs):
        context = {'form':{'AssetForm':AssetForm(),
        'StockForm':StockForm(), 
        'BondForm':BondForm(),
        'ExchangeTradedFundForm':ExchangeTradedFundForm()
        }}
        return super().get_context_data(**context)


# class CreateAsset(LoginRequiredMixin,View):
#     template_name = "portfolio/read.html"
#     form_class = AssetForm
#     success_url = "portfolio:createAsset"
#     context = None

#     def get(self,request):
#     return render(request, "todo/index.html", {'form':{'user':UserForm(),'todo':PostForm()}})

    # def post(self,request):
    #     form = self.form_class(data=request.POST)
    #     data=request.POST
    #     if form.is_valid(): 
    #         portfolio = Portfolio.objects.create(
    #             user = request.user,
    #             portfolio_name=data.get('portfolio_name')
    #             )
            
        
    #         return redirect(self.success_url)
    #     else:
    #         self.context = self.get_context(form)
    #         return self.render_to_response(request)


        
    # def get_context(self, form):
    #     return {
    #         "form": form,
    #         "action": "portfolio:create",
    #         "method": "POST",
    #         "submit_text": "Add new Portfolio"
    #     }

    # def render_to_response(self, request):
    #     return render(request, self.template_name, self.context)