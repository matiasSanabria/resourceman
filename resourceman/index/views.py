from django.shortcuts import render_to_response


def index(request):
    """
    Metodo que obtiene la vista del index del sistema
    :param request:
    :return: index del sistema
    """
    return render_to_response("index.html")
