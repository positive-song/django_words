from django.shortcuts import render
import pandas as pd
import random


# Create your views here.
def post_list(request):
    df = pd.read_csv('words.csv', encoding='cp949')
    words = df['word']
    word = random.choice(words)
    word2 = random.choice(words)
    return render(request, 'blog/post_list.html', {'abc': word, 'word2': word2})