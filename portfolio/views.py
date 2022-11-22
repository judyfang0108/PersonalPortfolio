from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Counting
from hitcount.views import HitCountDetailView
from django.contrib import admin

# Create your views here.


def home(request):
    context = {}
    return render(request, 'welcome.html', context)


class ProjectView(ListView):  # default view of main page
    model = Project
    template_name = 'projects.html'


class PortfolioView(HitCountDetailView):
    # 是否計算點擊
    count_hit = True
    # 使用的模組，預設使用 all 查詢
    # 如果要自訂查詢，可以用 get_queryset()，此屬性即可刪除
    model = Counting, Project
    # 使用的樣板
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """找不到 model 重導向到其他頁面範例
        若有需要再加即可，預設會跳 404 頁
        """

        # try:
        self.object = self.get_object()
        # except Http404:
        #     # 找不到 model
        #     return redirect('index')

        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """另外要傳給樣板的資料"""
        project_list = Project.objects.all()
        test = project_list[0].title
        context = super().get_context_data(**kwargs)
        context.update({
            'project_list': project_list,
        })
        return context

    def get_queryset(self):
        """自訂 model 查詢"""

        return Counting.objects.filter(show=True, id=self.kwargs.get('pk'))
