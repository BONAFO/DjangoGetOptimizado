from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import JsonResponse
from django.views.generic import View
from apps.cosa.models import Cosa
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from resorces.array import push,queryset_to_arr
# def cosaView2(request):
#     if request.method == "GET":
#         # print(1111)
#         # print(request.user.get_all_permissions())
#         if  request.user.has_perm("cosa.view_cosa"):
#             return JsonResponse({"datra": 123})
#         else:
#             return JsonResponse({"err": 1})
        
#         # user = authenticate(username="bona", password="polaco98")
#         # print(user)
#         # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        
        # if  request.user.has_perm("cosa.view_cosa"):
# @method_decorator(permission_required('cosa.view_cosa', raise_exception=True), name='dispatch')
# class cosaView2(View):
#     paginate_by = 15
#     model = Cosa
    
    
    
#     template_name = 'cosa.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # Crear url con filtros para mantener el paginador
    #     base_url = self.request.build_absolute_uri('/cosa/cosa?')
    #     url = self.request.build_absolute_uri(self.request.get_full_path())
    #     query = "SELECT * FROM Client_table ORDER BY ID OFFSET "+ 1 + " ROWS FETCH NEXT " + 5+" ROWS ONLY"

        
        
    #     # url = getRoute(self, self.request.build_absolute_uri(self.request.get_full_path()))
    #     # print(url)
        
    #     context["title"] = 'Listado de productos'
    #     context["active"] = True
    #     context["url"] = url
    #     context["segment"] = 'inventario productos'
    #     return context

    # def get_queryset(self):

    #     queryset = Cosa.objects.all().order_by('id')
        
    #     # if 'search' in self.request.GET:
    #     #     try:
    #     #         queryset = Producto.objects.filter(numero_serie = self.request.GET.get('search'))
    #     #     except Exception as e:
    #     #         queryset = Producto.objects.none()
    #     #     return queryset

    #     # if 'filter' in self.request.GET:
    #     #     filters = getFilters(self)
    #     #     queryset = Producto.objects.all().filter(**filters)
    #     #     return queryset

    #     return queryset


# user = authenticate(username="john", password="secret")
#  login(request, user)



# @permission_required(login_url="/", perm="cosa.view_cosa", raise_exception=True)
# def cosaView2(request):
#     if request.method == "GET":
        
#         # queryset = Cosa.objects.all().values("id").order_by('id')
        
#         # print(request.user.get_all_permissions())
#         # user = authenticate(username="bona", password="polaco98")
#         # print(user)
#         # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#         return JsonResponse(data={"name" : "Kururum jru ur uruuuru rururu"})
    
@permission_required(login_url="/", perm="cosa.view_cosa", raise_exception=True)
def cosaView(request):
    if request.method == "GET":
        ajax_query = request.GET.get("q")
        if not ajax_query is None and ajax_query == "t":
            context = {}
            page = int(request.GET.get("page") or 1)
            paginate_by = int(request.GET.get("paginate") or 10)
            data = Cosa.objects.all().values("id").order_by('id')
            
            ids = paginate_content(actual_page=page - 1, content=data, limit=paginate_by)
            ids_to_search = []
            for d in ids:
                push(ids_to_search, d['id'])
            queryset = Cosa.objects.filter(id__in=ids_to_search)
            context['content']  = queryset_to_arr(queryset)
            return JsonResponse(data=context)
        else:
            return render(request,template_name="cosa.html")
        # queryset = Cosa.objects.all().values("id").order_by('id')
        
        # print(request.user.get_all_permissions())
        # user = authenticate(username="bona", password="polaco98")
        # print(user)
        # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        
def paginate_content (content, limit, actual_page):
    pair =[limit * actual_page, limit * (actual_page + 1)]
    return content[pair[0]: pair[1]]
    # if content.count() <= actual_page * limit:
    

# def cosa():
#     page=2
#     paginate_by = 10
#     data = Cosa.objects.all().values("id").order_by('id')
#     ids = paginate_content(actual_page=page - 1, content=data, limit=paginate_by)
#     ids_to_search = []
    
#     for d in ids:
#         push(ids_to_search, d['id'])
#     queryset = Cosa.objects.filter(id__in=ids_to_search)
#     content = queryset_to_arr(queryset)
    
    
# cosa()