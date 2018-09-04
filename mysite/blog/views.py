from django.shortcuts import render
import pandas as pd
import random


# Create your views here.
def post_list(request):
    df = pd.read_csv('words.csv', encoding='cp949')
    words = df['word']

    # 단어 & 뜻 선택
    word = random.choice(words)
    meaning = df[words == word]['meaning'].values[0]

    # 다른 보기 만들기
    other = random.sample(set(df[df['meaning'] != meaning]['meaning']), 3)

    # 진짜 뜻을 추가
    other.append(meaning)
    random.shuffle(other)

    return render(request, 'blog/post_list.html', {'word': word, 'definition': other, 'correct': meaning})