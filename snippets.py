# ---django

# Добавление локальных настроек в django через файл local_settings.py
try:
    from ask.local_settings import *
except ImportError:
    pass

# Получение GET и POST параметров
order = request.GET['sort'] # опасно! Выдаст исключение, если нет значения с ключом page
if order == 'rating':
    queryset = queryset.order_by('rating')  # Проверка, что передано валдное значение
page = request.GET.get('page') or 1 # Не выдаст эксепшн, если нет значения с ключом page, а вернет None
try:
    page = int(page)    # Проверка, что передано число, если нет - BadRequest
except ValueError:
    return HttpResponseBadRequest()

# Находит директорию проекта, которая устанавливается в BASE_DIR переменную. От неё считаем все пути
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Получение IP адреса клиента
user_ip = request.META.get('HTTP_X_REAL_IP')
if user_ip in None:
    user_ip = request.META.get('REMOTE_ADDR')

# Работа с куками
response = HttpResponse(html)
response.set_coockie('visited', '1')

is_visited = request.COOKIES.get('visited')
