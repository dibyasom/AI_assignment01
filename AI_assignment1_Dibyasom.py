import numpy as np
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as py

result = list()

def cleanify(str):
    return str.lower().strip().split()

a,b,c = [],[],[]
for i in range(8):
    binary = bin(i)[2:].rjust(3,'0')
    a.append(bool(int(binary[0])))
    b.append(bool(int(binary[1])))
    c.append(bool(int(binary[2])))

a = np.array(a)
b = np.array(b)
c = np.array(c)

dataset = ["I am a human being","I am good","Good graders study well","Humans love graders","Every human does not study well"]
dataset = list(map(cleanify , dataset))
data = list()

#checkfor = input("Type in the keyword, which prcisely relates both the conditons: ")
checkfor = 'study' #since I'm already aware of the input :)


# Isolating the usable data.
for item in dataset:
    data += [item for temp in item if temp == checkfor]
    
for item in data:
    if (item.count('no')+item.count('not'))%2:
        print(item," ~~Negative !")
        result = np.logical_and(a, result)
        
    else:
        print(item," ~~Positive !")
        result = np.logical_and(b, c)
            
query = input("Type your query: ").lower().strip()
if query[-1]=='?':
    print("Humanity(A)\tStudies?\tGoodGrader?\tOutput~")
    for i in range(8):
        print(str(a[i])+'\t'*2+str(b[i])+'\t'*2+str(c[i])+'\t'*2+str(result[i]))
    
    result = list(map(str, result))
    resultf = result.count('False')-4
    resultt = result.count('True')
    
    if resultt==4:
        print("Result: YES")
    else:
        print("Inference: It's a contingency!")
        print("Result: NO")
        
    #Visualizing the set!    
    venn3(subsets = (1, 0, 1,0, 2, 0, 0), set_labels = ('Human', 'Study well', 'Do not study well'), alpha = 0.5);
    c = venn3_circles(subsets = (1, 0, 1, 0, 2, 0, 0), linestyle='dashed', linewidth=1, color='grey')
    c[0].set_lw(5.0)
    c[1].set_lw(2.0)
    c[2].set_lw(2.0)
    py.title("Venn representation of the scenario!")
    py.show()


