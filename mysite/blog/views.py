from django.shortcuts import render
import pandas as pd
import random
import csv
from django.views.decorators.csrf import csrf_protect


class AnswerSheet:
    word_list = []

    def get_words(self, word):
        self.word_list.append(word)


# Create your views here.
@csrf_protect
def post_list(request):
    df = pd.read_csv('words.csv', encoding='cp949')
    words = df['word']

    # 단어 & 뜻 선택
    word = random.choice(words)

    # 중복되면 넘어가도록 설정해야함
    answers = AnswerSheet()
    if len(answers.word_list) == len(words):
        return render(request, 'blog/finish.html')
    if word in answers.word_list:
        while word in answers.word_list:
            word = random.choice(words)
            if word not in answers.word_list:
                break

    answers.get_words(word)

    meaning = df[words == word]['meaning'].values[0]

    # 다른 보기 만들기
    choices = random.sample(set(df[df['meaning'] != meaning]['meaning']), 3)
    choices.append(meaning)
    random.shuffle(choices)


    wrong = []
    if request.method == 'POST':
        print(word)
        wrong.append(word)
        with open('wrong_words.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(wrong)

    return render(request, 'blog/post_list.html', {'word': word, 'definition': meaning, 'choices': choices})
