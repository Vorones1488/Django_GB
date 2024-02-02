from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)



def index(request):
    logger.info('переход на главную страницу')
    return HttpResponse(
        '''<h1>Приветствую это моя первое приложение на джанго</h1>
    <h3>Меня зовут Михаил и я ничего не понимаю )))</h3>'''
    )


def about(request):
    logger.info('переход на страницу обомне')
    return HttpResponse('''
    <h1> Я миша мне почти 37 годиков </h1>
    <p>Я занимаюсь спортом много работа и в свободное время пытаюсь осилить программирование на python</p>
    ''')
# Create your views here.
