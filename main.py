import arrays as ry
import random as rd


def init():
    arr = ry.get_PREHISTORIC_CULTURE()  #here, set the array u want to study
    ipt1 = input("Study or Results? \n").lower()
    if ipt1 == "study":
        ipt2 = input("Write or Learn \n")
        if (ipt2.lower() == "write"):
            write(arr)
        elif (ipt2.lower() == "learn"):  #elif bc maybe more stuf l8r?
            learn(arr)
    elif ipt1 == "results":  #dont test this out im too exhausted to write it
        seeFreqWrong(arr)


def write(arr):
    print("Write: " + "\n")
    if (len(arr) == 0):
        return
    for idx in reversed(range(len(arr))):
        print(" ")
        ax = arr[idx]
        print(ax[0])
        s = input("Definition: ")
        if (s == ax[1]):  #if correct
            arr.remove(ax)

        else:
            print("The answer was " + ax[1])
            t = input("Right or Wrong: ")  #manual check
            if (t == "Right" or t == "right"):
                arr.remove(ax)
            else:
                input("Type it again: ")
    write(arr)


def mcq(arr):
    print("MCQ: " + "\n")
    if (len(arr) == 0):
        return
    for idx in reversed(range(len(arr))):
        print('\n')
        ans = arr[idx]  #ANSWER ARRAY
        print("Term: " + ans[0])  #term
        #MCQ Logic:
        #create defidx array that stores all the possible answers
        defidx = [ans]  #store the term array
        for i in range(3):  #add 3 more values
            length = len(arr) - 1  #index is -1
            int = rd.randint(0, length)  #random index
            while (int == idx):
                int = rd.randint(0, length)  #ensures int!=indx
            defidx.append(arr[int])
        #create the A B C D arrays
        #A
        a_idx = rd.randint(0, 3)  #index of A term
        a = ['A', defidx[a_idx], False]  #add term to the A array
        a[2] = (a[1] == ans)  #is the ans right
        defidx.remove(defidx[a_idx])  #remove that term
        #B
        b_idx = rd.randint(0, 2)
        b = ['B', defidx[b_idx], False]
        b[2] = (b[1] == ans)
        defidx.remove(
            defidx[b_idx])  #this is inefficient but whatever it works
        #C
        c_idx = rd.randint(0, 1)
        c = ['C', defidx[c_idx], False]
        c[2] = (c[1] == ans)
        defidx.remove(defidx[c_idx])
        #D
        d = ['D', defidx[0], False]
        d[2] = (d[1] == ans)

        answers = [a, b, c, d]  #letter, array, boolean
        for i in answers:  #i is a, b, c, d
            print(i[0] + ": " + i[1][1])
            if (i[2] == True):
                correct = i  #the correct array is called correct
        ans_ltr = input("Answer: ").upper()
        if (ans_ltr == correct[0]):
            arr.remove(ans)
        else:
            print("The right answer was " + correct[0])


def learn(arr):
    mcq(arr)
    write(arr)


def seeFreqWrong(arr):
    print("High Diff" + '\n')
    for i in arr:
        if i[2] == 2: print(i[0] + ", " + i[1] + '\n')
    print("Mid Diff" + '\n')
    for i in arr:
        if i[2] == 1: print(i[0] + ", " + i[1] + '\n')


def credits():
    print("Made by @alissawu on github")
    print("not uploaded on git yet bc i barely use it")


#run
init()
