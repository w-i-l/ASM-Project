from math import log2
import time
import random

f = open("cuvinte_wordle.txt",'r')
out_txt = open("out.txt",'a')
# g = open("output.txt",'w',encoding='utf-8')
words = [x.strip() for x in f]
f = open("cuvinte_wordle.txt",'r')
words2 = [x.strip() for x in f]
# words = ["TAREI",'ZULIE', 'ZULUF', 'ZVELT']

best_word = ''
max_entropy = 0

def Entropy(word):
    patterns={}
    for x in words:
        pattern=''
        for i in range(5):
            if x[i]== word[i]:
                pattern+='🟩'
            elif word[i] in x:
                pattern+='🟨'    
            else:
                pattern+='⬜'
        if pattern in patterns:
            patterns[pattern]+=1
        else:
            patterns[pattern]=1
        # print(pattern)
    entropy=0
    for x in patterns:
        
        probability=patterns[x]/len(words)
        entropy+=probability*log2(probability)
    return -entropy

def find_best_word():
    global best_word,max_entropy

    best_word = ''
    max_entropy = 0

    for word in words:
        entropy = Entropy(word)

        if entropy > max_entropy and len(words)>1:
            best_word  = word
            max_entropy = entropy
        elif len(words) == 1:
            best_word = words[0]


def check_word(word,pattern):
    

    if len(pattern) <5:
        return 0
    # print(pattern)
    for i in range(5):
        if pattern[i] == '⬜':
            if best_word[i] in word:
                return 0
        elif pattern[i] == '🟨':
            #MAROI TAREI
            if best_word[i] == word[i]:
                return 0
            if best_word[i] not in word:
                return 0
        elif pattern[i] == '🟩':
            if not best_word[i] == word[i]:
                return 0
    return 1

            
def check_letters():
    global words

    f = open('output.txt',encoding='utf-8')

    pattern = f.readline()

    copie = words.copy()

    for word in copie:
        if check_word(word,pattern) == 0:
            words.remove(word)
    

def generate_structure(given_word,given_structure):
    for word in words:
        pattern = ''
        for i in range(5):
            if given_word[i] == word[i]:
                pattern += '🟩'
            elif given_word[i] in word:
                pattern += '🟨'
            else:
                pattern += '⬜'
        if pattern == given_structure:
            return word

def output_joc(chosen_word):
    g = open("output.txt",'w',encoding='utf-8')
    pattern = ''
    for i in range(5):
        if best_word[i] == chosen_word[i]:
            pattern += '🟩'
        elif best_word[i] in chosen_word:
            pattern += '🟨'
        else:
            pattern += '⬜'
    # print(pattern)
    g.write(pattern)
    return pattern

chosen_word = ''
# chosen_word = "ORALA"

response = ''

def wait_for_response():
    global response
    output_txt = open('output.txt','r+',encoding='utf-8')
    pattern = output_txt.read()
    output_txt.seek(0)
    while pattern == output_txt.read() or not(len(response)>0 and response[0]  in ['⬜','🟨','🟩']):
        # time.sleep(0.5)
        output_txt.seek(0)
        # print(output_txt.read())
        response = output_txt.read()
        
        output_txt = open('output.txt','r+',encoding='utf-8')
    
    output_txt.close()

def write_best_word():
     output_txt = open('output.txt','w',encoding='utf-8')
     output_txt.write(best_word)

def solve():
    global chosen_word,best_word,max_entropy,response

    wait_for_response()
    check_letters()
    find_best_word()
    write_best_word()
    # print(best_word,output_joc(chosen_word))
    
    # print(words)


    

best_word = "TAREI"

def tester(no_of_cases):
    global chosen_word,best_word,max_entropy,words

    before = time.time()

    teste_ok = 0
    nr_incercari = 0

    for i in range(no_of_cases):
        f.seek(0)
        words = [x.strip() for x in f]
        chosen_word = words2[i]
        best_word = 'TAREI'
        max_entropy = 0
        print('*'+chosen_word)
        out_txt.write('*'+chosen_word)
        # print("*TAREI")
        out_txt.write(" || TAREI")
        
        output_joc(chosen_word)
        i=1
        while not chosen_word == best_word:
            solve()
            # print("*"+best_word)
            out_txt.write(" --> "+best_word)
            i += 1
        if chosen_word == best_word:
            teste_ok += 1
        nr_incercari += i
        # print("Incercari: ",i)
        
        # print("------------------------------------")
        out_txt.write("\n")
    print("Incercari ok: ",teste_ok)
    print("Incercari: ",nr_incercari/no_of_cases)
    print((time.time()-before)//60,"min ",(time.time()-before)%60,'sec')

def write_tarei():
    f = open('output.txt','w',encoding='utf-8')
    f.write("TAREI")


# output_txt = open('output.txt','r',encoding='utf-8')
# print(output_txt.read())
# print(response)
# tester(1)

# chosen_word = "IROSI"
# print('=='+chosen_word)

# output_txt = open('output.txt','w',encoding='utf-8')
# output_txt.write("TAREI")
# for x in range(3):
#     wait_for_response()
#     solve()
#     print(best_word)
# print(output_joc(chosen_word))
def auto():
    print("*TAREI")
    write_tarei()
    before = time.time()
    # output_joc(chosen_word)
    i=0
    while not response == '🟩🟩🟩🟩🟩':
        solve()
        print("*"+best_word,max_entropy)
        i += 1
    print("Incercari: ",i)
    print(time.time()-before)

auto()