import uuid


class UniqueVisitorMiddleware:
    """
    Этот middleware создает новый уникальный идентификатор с помощью модуля uuid, если его нет в куках пользователя,
    и устанавливает его в куки. Затем он продолжает выполнение запроса. Если уникальный идентификатор уже есть в куках,
    middleware просто выполняет запрос.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'unique_visitor_id' not in request.COOKIES:
            unique_visitor_id = str(uuid.uuid4())
            response = self.get_response(request)
            response.set_cookie('unique_visitor_id', unique_visitor_id)
        else:
            response = self.get_response(request)
        return response


class HostnameMiddleware:
    """
    Благодаря этому middleware во всех запросах будет доступен атрибут request.hostname, который будет содержать первую
    часть HTTP-хоста.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hostname = request.META.get('HTTP_HOST', '').split(':')[0]
        request.hostname = hostname
        response = self.get_response(request)
        return response