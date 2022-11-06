from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse


class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({"id": f'{request.user.id}',
                                 "username": f'{request.user.username}',
                                 "email": f'{request.user.email}',
                                 "first_name": f'{request.user.first_name}',
                                 "last_name": f'{request.user.last_name}'})
        else:
            return HttpResponse('UNAUTHORIZED', status=401)

