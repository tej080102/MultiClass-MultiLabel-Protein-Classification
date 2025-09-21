
import numpy
import math
i=0
numpy.set_printoptions(threshold=numpy.inf)
numpy.set_printoptions(suppress=True, formatter={'float': '{:0.10f}'.format})
'''
load the labels for a database. 
label_file - a string containing the path to the text file containing 2 columns, the 
  first column is the label (an integer), second column is the protein sequence (string).
'''
def load_labels(label_file):
    f = open(label_file)
    labels = {}
    for line in f:
        toks = line.split()
        labels[toks[1].upper()] = int(toks[0])
    return labels

'''
parse a HHBLITS hmm file and return the contents.
fname - a string containing the path to the hmm text file output by HHBLITS
returns:
seq - the protein sequence
prob - the linear probabilties
extras - ten probabilites for each state about insertions, deletions, etc.
'''
def parse_hmm(fname,outname,str1):
    f = open(fname)
    line=f.readline()
    while line[0]!='#':
        line=f.readline()   
    f.readline()
    f.readline()
    f.readline()
    f.readline()    
    seq = []
    extras = numpy.zeros([0,10])
    prob = numpy.zeros([0,20])
    line = f.readline()
    while line[0:2]!='//':
        lineinfo = line.split()
        seq.append(lineinfo[0])  
        probs_ = [2**(-float(lineinfo[i])/1000) if lineinfo[i]!='*' else 0. for i in range(2,22)]
        prob = numpy.concatenate((prob,numpy.matrix(probs_)),axis=0)
        
        line = f.readline()
        lineinfo = line.split()
        extras_ = [2**(-float(lineinfo[i])/1000) if lineinfo[i]!='*' else 0. for i in range(0,10)]
        extras = numpy.concatenate((extras,numpy.matrix(extras_)),axis=0)
        
        line = f.readline()
        assert len(line.strip())==0
        
        line = f.readline()
        # print(prob)
        # filepath =r"E:\Research\PSCL_Work\Dataset\HMM_Extract\Independent\Train_hmm_parsed\1.txt"
        
        numpy.savetxt(outname, prob, delimiter=",", fmt='%f')
        # print(prob.shape)    
    print(i,':',prob.shape)
    str1+=f'{i}:{prob.shape}'
    str1+='\n'
    return str1
    

'''
parse a PSIBLAST pssm file and return the contents.
fname - a string containing the path to the pssm text file output by PSIBLAST
returns:
seq - the protein sequence
prob - the linear probabilties, divided by 100
lprob - the log probabilities
'''
# def parse_pssm_sigmoid(fname):
#     f = open(fname)
#     # the 4th line should be the start of the PSSM data
#     f.readline()
#     f.readline()
#     f.readline()
#     seq = []
#     lprob = numpy.zeros([0,20])
#     prob = numpy.zeros([0,20])
#     line = f.readline()
# #     print(fname)
#     while len(line.strip())>0:
#         lineinfo = line.split()
#         seq.append(lineinfo[1])
        
#         lprobs_ = [float(1 / (1 + math.exp(-1*float(lineinfo[i]) ))) for i in range(2,22)]
#         lprob = numpy.concatenate((lprob,numpy.matrix(lprobs_)),axis=0)
#         probs_ = [float(1 / (1 + math.exp(-1*float(lineinfo[i]) ))) for i in range(22,42)]
# #         print(probs_)
#         prob = numpy.concatenate((prob,numpy.matrix(probs_)),axis=0)
#         line = f.readline()
    
#     return (''.join(seq),prob,lprob)

# def parse_pssm_tanh(fname):
#     f = open(fname)
#     # the 4th line should be the start of the PSSM data
#     f.readline()
#     f.readline()
#     f.readline()
#     seq = []
#     lprob = numpy.zeros([0,20])
#     prob = numpy.zeros([0,20])
#     line = f.readline()
# #     print(fname)
#     while len(line.strip())>0:
#         lineinfo = line.split()
#         seq.append(lineinfo[1])
        
#         lprobs_ = [float( math.tanh(float(lineinfo[i]) )) for i in range(2,22)]
#         lprob = numpy.concatenate((lprob,numpy.matrix(lprobs_)),axis=0)
#         probs_ = [float( math.tanh(float(lineinfo[i]) )) for i in range(22,42)]
# #         print(probs_)
#         prob = numpy.concatenate((prob,numpy.matrix(probs_)),axis=0)
#         line = f.readline()
    
#     return (''.join(seq),prob,lprob)

# def parse_pssm(fname):
#     f = open(fname)
#     # the 4th line should be the start of the PSSM data
#     f.readline()
#     f.readline()
#     f.readline()
#     seq = []
#     lprob = numpy.zeros([0,20])
#     prob = numpy.zeros([0,20])
#     line = f.readline()
#     while len(line.strip())>0:
#         lineinfo = line.split()
#         seq.append(lineinfo[1])
#         lprobs_ = [float(lineinfo[i]) for i in range(2,22)]
#         lprob = numpy.concatenate((lprob,numpy.matrix(lprobs_)),axis=0)
#         probs_ = [float((float(lineinfo[i])+0.05)/100.05) for i in range(22,42)]
#         prob = numpy.concatenate((prob,numpy.matrix(probs_)),axis=0)
#         line = f.readline()
    
#     return (''.join(seq),prob,lprob)
str1=""
for i in range(0,28304):
    
    fname=f'/raid/home/tejus/MLMC/Dataset_1/HMM/Train_hmm/{i}.txt'
    outname=f'/raid/home/tejus/MLMC/Dataset_1/HMM/Train_hmm_parsed/{i}.csv'
    with open (outname,'w+') as f1: 
        str1=parse_hmm(fname,outname,str1)
    f1.close()
    
with open('/raid/home/tejus/MLMC/Dataset_1/HMM/Train_hmm_parsed/shape.txt','w+') as g:
    g.write(str1)
g.close()