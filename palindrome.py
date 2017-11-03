def clean2(s):
    ch=[' ',',','.','!','-','?','"',"'",';',':','(',')']
    for c in ch:
        s=s.replace(c,'')
    return s.lower()

def isPal2(s):
    if(len(s)<=1):#base case
        return True
    else:#recursive case
        return((s[0]==s[-1]) and isPal2(s[1:-1]))

def clean(s):
    #manual cleaning not using replace
    out=''
    for i in range(len(s)):
        if(s[i] in [' ',',','.','!','-','?']):
            pass
        else:
            out+=(s[i].lower())
            #out+=s[i]
    return out

def isPal(s):
    #print(s[0])
    #s=s.replace(" ","")
    #print('calling ispal on ',s)
    if(len(s)==1):#base case
        return True
    elif(len(s)==2):#base case
        if(s[0]==s[1]):
            return True
        else:
            return False
    else:#recursive case
        if(s[0]==s[len(s)-1]): #outside check
            flag=True
        else:
            flag=False
        inside=[]#create inside
        for i in range(1,len(s)-1,1):
            inside.append(s[i])
        inside=''.join(inside)
        #print('inside is',inside)
        return(flag and isPal(inside))

def main():
    #print(isPal(clean('adA')))
    #print(isPal('hello'))
    #print(isPal(clean('r  a c     e ca r')))
    #print(clean('Sg   u f SSuS'))
    print(isPal(clean('raceecar')))
    print(isPal(clean('racecar')))

    print()

def main2():
    print(isPal2(clean2('palindrome is I emordnilap')))
    print(isPal2(clean2('Barge in! Relate mere war of 1991 for a were-metal Ernie grab!')))
    print(isPal2(clean2('Are we not pure? "No sir!" Panama\'s moody Noriega brags. "It is garbage!" Irony dooms a man; a prisoner up to new era.')))
    print()

def main3():
    l=['Yo, bottoms up! (U.S. motto, boy.)',
    'A man, a plan, a canal: Panama.',
    'As I pee, sir, I see Pisa!',
    'Do good? I? No! Evil anon I deliver. I maim nine more hero-men in Saginaw, sanitary sword a-tuck, Carol, I -- lo! -- rack, cut a drowsy rat in Aswan. I gas nine more hero-men in Miami. Reviled, I (Nona) live on. I do, O God!',
    'Go hang a salami; I\'m a lasagna hog.',
    'Gateman sees name, garageman sees name tag.',
    'I roamed under it as a tired, nude Maori.',
    'T. Eliot, top bard, notes putrid tang emanating, is sad. I\'d assign it a name: gnat dirt upset on drab pot-toilet.',
    ]
    for i in l:
        print(isPal2(clean2(i)))

    print()
#main()
#main2()
#main3()

'''A dog, a plan, a canal: pagoda.
A man, a plan, a canal: Panama.
A new order began, a more Roman age bred Rowena.
A tin mug for a jar of gum, Nita.
A Toyota. Race fast, safe car. A Toyota.
Able was I ere I saw Elba.
Animal loots foliated detail of stool lamina.
Anne, I vote more cars race Rome to Vienna.
Are we not drawn onward, we few, drawn onward to new era?
Are we not pure? "No sir!" Panama's moody Noriega brags. "It is garbage!" Irony dooms a man; a prisoner up to new era.
As I pee, sir, I see Pisa!
Barge in! Relate mere war of 1991 for a were-metal Ernie grab!
Bombard a drab mob.
Bush saw Sununu swash sub.
Cain: a maniac.
Cigar? Toss it in a can. It is so tragic.
Daedalus: nine. Peninsula: dead.
Dammit, I'm mad!
Delia saw I was ailed.
Denim axes examined.
Dennis and Edna sinned.
Depardieu, go razz a rogue I draped.
Desserts, I stressed!
Did I draw Della too tall, Edward? I did?
Do good? I? No! Evil anon I deliver. I maim nine more hero-men in Saginaw, sanitary sword a-tuck, Carol, I -- lo! -- rack, cut a drowsy rat in Aswan. I gas nine more hero-men in Miami. Reviled, I (Nona) live on. I do, O God!
Doc, note I dissent: a fast never prevents a fatness. I diet on cod.
Drab as a fool, aloof as a bard.
Drat Saddam, a mad dastard!
Draw, O coward!
Draw pupil's lip upward.
Ed, I saw Harpo Marx ram Oprah W. aside.
Eva, can I stab bats in a cave?
Evil did I dwell; lewd I did live.
Gateman sees name, garageman sees name tag.
Go hang a salami; I'm a lasagna hog.
Goldenrod-adorned log.
Golf? No sir, prefer prison-flog.
Harass sensuousness, Sarah.
I roamed under it as a tired, nude Maori.
Laminated E.T. animal.
Lay a wallaby baby ball away, Al.
Lepers repel.
Let O'Hara gain an inn in a Niagara hotel.
Live not on evil.
Lived on Decaf; faced no Devil.
Lonely Tylenol.
Ma is a nun, as I am.
Ma is as selfless as I am.
Madam, I'm Adam.
Madam in Eden, I'm Adam.
Marge lets Norah see Sharon's telegram.
May a moody baby doom a yam.
Meet animals; laminate 'em.
Mr. Owl ate my metal worm.
Murder for a jar of red rum.
Never odd or even.
No, Mel Gibson is a casino's big lemon.
No cab, no tuna nut on bacon.
No lemon, no melon.
No sir -- away! A papaya war is on.
On a clover, if alive, erupts a vast, pure evil; a fire volcano.
Party boobytrap.
Poor Dan is in a droop.
Reviled did I live, said I, as evil I did deliver.
Rise to vote, sir.
Saw tide rose? So red it was.
Senile felines.
So many dynamos!
Some men interpret nine memos.
Stab nail at ill Italian bats.
Stack cats.
Stella won no wallets.
Step on no pets.
Stop! Murder us not, tonsured rumpots!
Straw? No, too stupid a fad; I put soot on warts.
T. Eliot, top bard, notes putrid tang emanating, is sad. I'd assign it a name: gnat dirt upset on drab pot-toilet.
Tarzan raised Desi Arnaz' rat.
Ten animals I slam in a net.
Too bad I hid a boot.
Was it a car or a cat I saw?
Wonder if Sununu's fired now.
Won't I panic in a pit now?
Won't lovers revolt now?
Yo, banana boy!
Yo, Bob! Mug o' gumbo, boy!
Yo, bottoms up! (U.S. motto, boy.)'''
