#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module
import os
import sys
import time

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

def Play_Cross(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 컵받침이 필요해. 깨지지 않는 종이나 나무로 된 컵받침을 준비해줘. ")
        text_to_speech("징검다리를 만들 수 있게 5개 보다 많이 준비하면 돼")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()    # stt open
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)   # stt 결과 처리 (NLP.py 참고)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("좋았어. 놀이 방법을 알려줄게!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
            continue
        break

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech("바닥에 컵받침을 뿌려서 징검다리를 만들고 하나씩 밟고 강을 건너 볼거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("강을 건널 때는 넘어지지 않게 조심해야해.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                text_to_speech("그래, 시작하자!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():
        behavior_list.do_explain_A()
        while True:
            time.sleep(1)
            text_to_speech("컵받침을 뿌려서 징검다리를 만들어 봐. 일자로 뿌려 놓으면 건너기가 쉬울거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    time.sleep(2)
                    text_to_speech("이제 징검다리를 하나씩 건너뛰면서 균형을 잡아보자. 하나씩 뛸 때마다 숫자를 세보는 거야.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("도착하면 도착했어 라고 알려줘.")
            #강물 흐르는 효과음
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("집중력이 정말 대단한걸?")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("돌이 몇 개 였어?")
            user_said = speech_to_text()
            

            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("그랬구나~ 정말 잘했어! ")
        
            break

        behavior_list.do_suggestion_L()
        while True:
            time.sleep(1)
            text_to_speech("이제 뒤로 돌아서 다시 징검다리를 건너보자. 이번엔 하나씩 뛸 때마다 거꾸로 숫자를 세어보는 거야.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("도착하면 도착했어 라고 알려줘.")
            time.sleep(1)
            #강물 흐르는 효과음

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech(f"정말 잘 했어. {user_name}이는 숫자도 잘 세고 균형도 잘 잡는 것 같아.")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_question_S()
    while True:
        text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':
            behavior_list.do_agree()
            while True:
                text_to_speech("그래 또 하자!")
                start()
        else:
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 파이보도 똑똑해진 것 같아!")
                break
        break

    # 2.5 마무리 대화

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 전에도 징검다리를 건너본 적이 있어?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나. 파이보는 징검다리를 보면 혹시나 물에 빠질까봐 마음이 조마조마해.")
        user_said = speech_to_text()
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 오늘 징검다리 건너는 게 어렵진 않았어?")
        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}가 열심히 놀이 하는 모습이 멋졌어~")
        
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 컵받침을 들고 브이를 해봐!")
        break

    behavior_list.do_photo()
    time.sleep(5)
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=False)

    # 2.7 다음 놀이 제안
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("또 다른 놀이 할까? 파이보랑 또 놀고 싶으면 놀고 싶다고 말해줘!")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':       # 지금은 어떤 답변이라도 프로그램 종료됨
            behavior_list.do_joy()
            while True:
                text_to_speech("그래 좋아!")
                time.sleep(1)
                break
        else:
            behavior_list.do_agree()
            while True:
                time.sleep(1)
                text_to_speech("다음에 또 놀자!")
                break
        break
