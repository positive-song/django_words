from django.shortcuts import render
import pandas as pd
import random


class AnswerSheet:
    word_list = []

    def get_words(self, word):
        self.word_list.append(word)


# Create your views here.
def post_list(request):
    df = pd.read_csv('words.csv', encoding='cp949')
    words = df['word']
    word = random.choice(words)


    ## 중복되면 넘어가도록 설정해야함

    answers = AnswerSheet()
    answers.get_words(word)

    meaning = df[words == word]['meaning'].values[0]

    # 다른 보기 만들기
    choices = random.sample(set(df[df['meaning'] != meaning]['meaning']), 3)
    choices.append(meaning)
    random.shuffle(choices)

    return render(request, 'blog/post_list.html', {'word': word, 'definition': meaning, 'choices': choices})
