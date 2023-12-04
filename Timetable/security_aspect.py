import aspectlib
from django.http import JsonResponse

@aspectlib.Aspect
def secure_resource_access(*args, **kwargs):
    view_function = args[0]  

    request = next((arg for arg in args if getattr(arg, 'user', None)), None)

    if not request or not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized access'}, status=401)

    result = yield aspectlib.Proceed
    return result

