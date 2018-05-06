def check_pure(L) :
    if check_pure_equal(L) :
        return True
    c = 0
    c = check_pure_half1(L) + c
    c = check_pure_half2(L) + c
    if c == 2 :
        return True
    else :
        return False

def check_pure_half2(L) :
    c = 0
    if len(L) == 4 :
        if L[0][0] == L[1][0] == L[2][0] == L[3][0] :
            c = c + 1
    if len(L) == 3 :
        if L[0][0] == L[1][0] == L[2][0]:
            c = c + 1
    if len(L) == 2 :
        if L[0][0] == L[1][0] :
            c = c + 1
    return c

def check_pure_equal(L) :

    if len(L) == 4 :
UMMY DECLARATION CHECKER== L[2] == L[3] :
            return True
    elif len(L) == 3 :
        if L[0] == L[1] == L[2]:
            return True
    elif len(L) == 2 :
        if L[0] == L[1]:
            return True
    else :
        return False


def check_pure_half1(L) :

    n = 0
    c = 0
    for i in range(0, len(L0)- 1) :
        if L[0][1] == L0[i] :
            for j in range(1, len(L)) :
                i = i + 1
                if i < len(L0) - 1 :
                    if(L[j][1] != L0[i]) :
                        n = n + 1
                        break
            if n == 0 :
                c = c + 1
                break
    return c


def check_jokers(L) :

    pos = []
    for i in range(0, len(L)) :
        if L[i] == "joker" :
            pos.append(i)
    return pos


def check_impure(L) :

    L_new = []
    L_new1 = []
    pos = []
    pos = check_jokers(L)

    if len(pos) == 1 :
        if pos[0] == 0:
            L_new = L[1 : len(L)]

            if check_pure(L_new) :
                return True

        if pos[0] == len(L) - 1 :
            L_new = L[0 : len(L) - 1]

            if check_pure(L_new) :
                return True

        if len(L) == 3 :


            if pos[0] == 1 :
                L_new = [x for x in L if x != "joker"]

                if position(L_new) == -2 and (check_pure_half2(L_new) or check_pure_equal(L_new)):
                    return True

        if len(L) == 4 :

            if pos[0] == 1 :
                L_new1.append(L[0])
                L_new1.append(L[2])
                L_new.append(L[2])
                L_new.append(L[3])
                t1 = position(L_new1)
                t2 = position(L_new)

                if t1 == -2 and t2 == -1 and (check_pure_half2(L_new1) or check_pure_equal(L_new1))and (check_pure_half2(L_new) or check_pure_equal(L_new)):
                    return True

            if pos[0] == 2 :
                L_new1.append(L[0])
                L_new1.append(L[1])
                L_new.append(L[1])
                L_new.append(L[3])
                t1 = position(L_new1)
                t2 = position(L_new)

                if t1 == -1 and t2 == -2 and (check_pure_half2(L_new1) or check_pure_equal(L_new1))and (check_pure_half2(L_new) or check_pure_equal(L_new)):
                    return True
    if len(L) == 4 :
        if len(pos) == 2:
            if pos[0] == 0 and pos[1] == 3 :
                L_new = [x for x in L if x != "joker"]
                if check_pure(L_new) :
                    return True
            if (pos[0] == 0 and pos[1] == 2) or (pos[0] == 1 and pos[1] == 3):
                L_new = [x for x in L if x != "joker"]
                if position(L_new) == -2 and (check_pure_half2(L_new) or check_pure_equal(L_new)):
                    return True

            if pos[0] == 1 and pos[1] == 2 :
                L_new = [x for x in L if x != "joker"]
                if position(L_new) == -3 and (check_pure_half2(L_new) or check_pure_equal(L_new)):
                    return True
    return False
 

def position(L) :
    n = 0
    for i in range(0, len(L0)) :
        if L[0][1] == L0[i] :
            pos1 = i
            for j in range(pos1 + 1, len(L0)) :
                if i < len(L0):
                    if  L[1][1] == L0[j] :
                        pos2 = j
                        n = n + 1
                        break;
            if n != 0 :
                break
            if n == 0 :
                return False
    return (pos1 - pos2)

def check_set(L) :
    c = 0
    j = check_jokers(L)
    if len(j) == 0 :
        if L[0][1] == L[1][1] == L[2][1] :
            c = c + 1
        if (L[0][0] != L[1][0] and L[0][0] != L[2][0] and L[1][0] != L[2][0]) :
            c = c + 1
        if c == 2 :
            return True
        
    if len(j) == 1 :
        L_new = [x for x in L if x != "joker"]
        if L_new[0][1] == L_new[1][1] :
            c = c + 1
        if L_new[0][0] != L_new[1] :
            c = c + 1
        if c == 2 :
            return True
    if len(j) == 2 :
        return True
    return False


def only_two_jokers(L) :
    c = 0
    for i in range(0, len(L)) :
        if L[i] == "joker" :
            c = c + 1
    return c

print("\n")
print("RUMMY DECLARATION CHECKER\n")
print("List1 = [H, S, D, C]\n")
print("""List2 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']\n""")
print("'joker' - Joker\n")
print("NOTE : T - value is 10\n")
print("""Take one element from List1 and and another from List2 as a string and it represents a card\n""")
print("Ex : H3 - Suit is Heart and Face value is 3\n""") 
print("NOTE : Only two Jokers are accepted\n")
L = []        
L0 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
L1 = []
L2 = []
L3 = []
L4 = []
while True :
    count = 0
    print("Please enter your LIFE1 of 4 cards on planck 1")
    st = input("By giving spaces b/w each card name\n")
    L1 = st.split()
    count = only_two_jokers(L1) + count
    if count > 2 :
        print("only two jokers are acceptable for a game")
        print("jokers were exceeded")
        continue
    if len(L1) == 4 :
        break
    else :
        print("Please enter  only 4 cards")

while True :
    print("Please enter your LIFE2 of 3 cards on planck 2")
    st = input("By giving spaces b/w each card name\n")
    L2 = st.split()
    count = count + only_two_jokers(L2)
    if count > 2 :
        print("only two jokers are acceptable for a game")
        print("jokers were exceeded")
        count = count - only_two_jokers(L2)
        continue
    if len(L2) == 3 :
        break
    else :
        print("Please enter only 3 cards")
while True :
    print("Please enter your LIFE or SET of 3 cards on planck 3")
    st = input("By giving spaces b/w each card name\n")
    L3 = st.split()
    count = count + only_two_jokers(L3)
    if count > 2 :
        print("only two jokers are acceptable for a game")
        print("jokers were exceeded")
        count = count - only_two_jokers(L3)
        continue
    if len(L3) == 3 :
        break
    else :
        print("Please enter  only 3 cards")

while True :
    print("Please enter your LIFE or SET of 3 cards on planck 4")
    st = input("By giving spaces b/w each card name\n")
    L4 = st.split()
    count = count + only_two_jokers(L4)
    if count > 2 :
        print("only two jokers are acceptable for a game")
        print("jokers were exceeded")
        count = count - only_two_jokers(L4)
        continue
    if len(L4) == 3 :
        break
    else :
        print("Please enter only 3 cards")

count1 = 0
L5 = []
if check_pure(L1) :
    L5.append("P")
if check_impure(L1) :
    L5.append("I")
if check_pure(L2) :
    L5.append("P")
if check_impure(L2) :
    L5.append("I")
if (check_pure(L3) or check_impure(L3) or check_set(L3)) :
    count1 = count1 + 1
    L5.append(count1)
if (check_pure(L4) or check_impure(L4) or check_set(L4)) :
    count1 = count1 + 1
    L5.append(count1)

if L5 == ["P", "I", 1, 2] or L5 == ["I", "P", 1, 2] or L5 == ["P", "P", 1, 2]:
    print("Congratulations! You Completed the SHOW")
else :
    print("Sorry, You cards don't make any SHOW")
