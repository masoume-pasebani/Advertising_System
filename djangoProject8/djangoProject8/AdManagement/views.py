from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, FormView, base, DetailView
from .models import Ad, Advertiser, View, Click
from .forms import Form
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


# def showAds(request):
#     advertisers = Advertiser.objects.all()
#     context = {"advertisers": advertisers}
#
#     # increase ads views
#     ads = Ad.objects.all()
#     for ad in ads:
#         view = View.objects.create(
#             view_date=datetime.now(),
#             user_ip=request.META['REMOTE_ADDR'],
#             ad=ad
#         )
#         view.save()
#
#     return render(request, 'advertiser_management/ads.html', context)

class ShowAds(base.TemplateView):
    template_name = 'ads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()

        # increase ads views
        ads = Ad.objects.all()
        for ad in ads:
            view = View.objects.create(
                ip=self.request.META['REMOTE_ADDR'],
                ad=ad
            )
            view.save()

        return context


class CountClickAndRedirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'count-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        click = Click.objects.create(
            ip=self.request.META['REMOTE_ADDR'],
            ad=ad
        )
        click.save()
        self.url = ad.Link
        return ad.Link


class AdFormView(FormView):
    form_class = Form
    template_name = 'form.html'

    def form_valid(self, form):
        advertiser_id = form.cleaned_data.get("advertiser_id")
        image = form.cleaned_data.get("Img")
        title = form.cleaned_data.get("Title")
        link = form.cleaned_data.get("Link")
        ad = Ad.objects.create(
            Title=title,
            Img=image,
            Link=link,
            Adv=get_object_or_404(Advertiser, pk=advertiser_id)
        )
        ad.save()
        return HttpResponseRedirect(reverse('show-ads'))


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad-detail.html'