# -*- coding: cp949 -*-
from __future__ import division
import math
import random
import pprint


def sigmoid(a):
    #시그모이드 함수로 tanh 함수 사용
    return math.tanh(a)/2 + 0.5

def rand(a, b):
    # a <= rand < b
    return (b-a)*random.random() + a

def nn_activation(nn_input,nn_weight,bias = -1):
    #nn_input 과 nn_weight 는 리스트
    if len(nn_input) != len(nn_weight)-1:
        print '입력값과 가중치의 수가 맞지 않음'
        exit()
    nn_len = len(nn_input) + 1
    nn_input = nn_input + [bias]
    activation = 0
    for n in range(nn_len):
        activation = activation + nn_input[n] * nn_weight[n]
    return sigmoid(activation)

############예제###############
#nn_input = [1,0,1,1,0]
#nn_weight = [0.5,-0.2,-0.3,0.9,0.1]
#test = nn_activation(nn_input,nn_weight)
#print test
#여기서 test는 1.1 이 되어야 한다
############예제###############

def make_list(m,n):
    #여러 용도로 만드는 리스트(2차원 배열)
    #n 은 세로 m은 가로
    l1 = []
    l2 = []
    for tmp1 in range(n):
        for tmp2 in range(m):
            l2 = l2 + [0]
        l1.append(l2)
        l2 = []
    return l1

############예제###############
#import pprint
#t = make_list(4,7)
#pprint.pprint(t)
#결과
#[[0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0]]
############예제###############

def make_nn(n_input,n_hidden,n_output,init_weight = 0.2):
    #입력값의 수 , 히든레이어의 뉴런수, 출력의 수, 초기 가중치 랜덤 범위
    #가중치는 대충 랜덤으로 책정
    nn_hidden = make_list(n_input+1,n_hidden)
    nn_output = make_list(n_hidden+1,n_output)
    for a in range(n_input+1):
        for b in range(n_hidden):
            nn_hidden[b][a] = rand(-init_weight,init_weight)
    for a in range(n_hidden+1):
        for b in range(n_output):
            nn_output[b][a] = rand(-init_weight,init_weight)    
    return [nn_hidden,nn_output]


def cpu(l_input,l_nn):
    tmp1 = []
    for x in l_nn[0]:
        tmp1 = tmp1 + [nn_activation(l_input,x)]
    print tmp1
    tmp2 = []
    for x in l_nn[1]:
        tmp2 = tmp2 + [nn_activation(tmp1,x)]
    print tmp2

def fix(l_input,l_answer,l_hidden,l_output,l_nn,alpha = 0.1):
    #입력값 리스트,정답리스트,히든레이어의 출력값리스트,실제 출력층의 출력리스트,뉴런,민감도
    #가중치 조정, 리턴값은 l_nn
    #먼저 출력-은닉 가중치 수정
    error_out = []
    for x in range(len(l_answer)):
        error_out = error_out + [(l_answer[x] - l_output[x]) * l_output[x] * (1 - l_output[x])]
        print 'error_out -> ',error_out
        for y in range(len(l_nn[1][x])):#y에는 가중치의 번호? 가 들어가 있음
            l_nn[1][x][y] = l_nn[1][x][y] + alpha * error_out[x] * l_hidden[y] #가중치 조정
    #다음으로 입력-은닉 가중치 수정
    for x in range(len(l_nn[0])):#히든레이어의 뉴런수
        #에러 = 뉴런의 출력(1-뉴런의 출력) * 시그마(1~출력뉴런의 수)(출력뉴런의 에러*히든뉴런과 출력뉴련의 가중치)
        sum = 0
        for tmp in range(len(error_out)):
            sum = sum + error_out[tmp] * l_nn[1][tmp][x]
        error_hidden = error_out[x] * (1 - error_out[x]) * sum
        print 'error_hidden -> ',error_hidden
        for y in range(len(
            
            
            
            
        error_hidden = l_hidden[x] * (1 - l_hidden[x])
        

    
    return l_nn


def train(l_input,l_answer):
    
fail.py
