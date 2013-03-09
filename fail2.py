# -*- coding: cp949 -*-

#원본 벡프로파게이트 함수가 날라감... 그래서 bpnn껄 수정해 넣음 그래도 안되는건 매한가지
#왜이럴까....
from __future__ import division
import math
import random
import pprint
random.seed()

def sigmoid(x):
    return math.tanh(x)

#시그모이드 함수의 미분함수
def dsigmoid(y):
    return 1.0 - y**2

def rand(a, b):
    # a <= rand < b
    return (b-a)*random.random() + a

def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

class nn:
    def __init__(self,ni,nh,no):
        #입력수,히든수,출력수
        self.ni=ni+1
        self.nh=nh
        self.no=no

        self.ah=[1.0]*self.nh
        self.ao=[1.0]*self.no

        self.wh=makeMatrix(self.ni,self.nh)
        self.wo=makeMatrix(self.nh,self.no)
        
        for x in range(self.nh):
            for y in range(self.ni):
                self.wh[y][x] = rand(-2.0, 2.0)
        for x in range(self.no):
            for y in range(self.nh):
                self.wo[y][x] = rand(-0.2, 0.2)
                
        self.ch = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def calc(self,l_input):
        #입력값에 대한 출력값 계산
        if len(l_input) is not self.ni-1:
            print 'error',2
            exit()
        #히든 레이어의 activation 구함
        l_input=l_input+[1.0]
        self.ai=[]
        for x in l_input:
            self.ai = self.ai + [x]
        for x in range(self.nh):
            sum=0
            for y in range(self.ni):
                sum = sum + self.wh[y][x]*l_input[y]
            self.ah[x]=sigmoid(sum)

        #출력 레이어의 activation(=출력값)을 구함
        for x in range(self.no):
            sum=0
            for y in range(self.nh):
                sum = sum + self.wo[y][x]*self.ah[y]
            self.ao[x]=sigmoid(sum)
        return self.ao

    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.calc(p[0]))

    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ah[i]
                self.wh[i][j] = self.wh[i][j] + N*change + M*self.ch[i][j]
                self.ch[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error
    
    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.calc(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                print('error %-.6f' % error)

a=nn(2,4,1)
pat = [
    [[0,0], [1]],
    [[0,1], [0]],
    [[1,0], [0]],
    [[1,1], [1]]
]
a.train(pat)
a.test(pat)
