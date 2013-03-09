import random

def create_cluster(input_num, layer, synaps_weight1, synaps_weight2):
    if synaps_weight1 > synaps_weight2:
        print "weight1 must be smaller than weight2!"
        break

    threshold = (synaps_weight1+synaps_weight2)/2
    keuron[0][0]="output"
    for i in range(1,layer):
        for j in range(0,input_num):
            keuron[i][j]=[threshold, random.sample(range(-10000,10000),1), 
