import sys
from collections import deque

def preferenceCheck(numPeople, preferenceList, womanI, manI, currentPartnerI) :
    '''
    This method checks the preference of the current woman chosen to see if she'd rather be with
    her current partner or with the new partner.
    '''
    for i in range(numPeople) :
        if(preferenceList[womanI][i] == currentPartnerI) :
            return 1
        #endif

        if(preferenceList[womanI][i] == manI) :
            return 0
        #endif
    #endfor
#enddef

    
def stableMatching(numMenWomenI, menPrefList, womenPrefList) :
    '''
    This function recieves the number of matches to be made, as well as the preference of each man and woman.
    It goes through each man checks the preference, and engages the two if the woman isn't already engaged.
    If the woman is engaged, it checks her preferences to see if she'd rather be with her current partner
        or with the man that seeks to be with her.
    Engaged is a List of Lists. Each list in engaged will hold the engaged couple.

    The values are shifted down by one for easy indexing in the menPrefList and womenPrefList.
    '''

    ## Stores partner of women.
    wPartner = [(0, False)] * numMenWomenI
    
    ## Stores availability of men.
    mFree = deque()
    for x in range(numMenWomenI):
        mFree.append(x)
    #endfor

    ## Stores engaged pairs
    engaged = []
    
    i = 0
    while(mFree):

        # Get the first free man
        m = mFree.popleft()
        mList = menPrefList[m]

        # Highest-ranked in m's preferences
        w = mList[i]
        # print("Chose Female", w)

        # If the woman is free, engage m and w
        if(wPartner[w][1] == False) :
            wPartner[w] = (m, True)
            engaged.append([m, w])
            i = 0
        # If the woman is not free, check her preference list
        else:
            # Get current partner
            m1 = wPartner[w][0]

            # Get the indicies of current partner and new man
            m1index = womenPrefList[w].index(m1)
            mindex = womenPrefList[w].index(m)

            # If the new man's index is less, then switch engagement and free the current partner
            if(mindex < m1index):
                wPartner[w] = (m, True)
                mFree.appendleft(m1)
                engaged.append([m, w])
                engaged.remove([m1, w])
                i = 0
            else:
                mFree.appendleft(m)
                i = i + 1
            #endif
        #endifelse
    #endwhile

    return (engaged)
#enddef

def main() :
    menPrefList = []
    womenPrefList = []

    if len(sys.argv) < 2 :
        print('error: incorrect format')
        print('Try: python stable_matching_2800144.py inputfile.txt')
        sys.exit(0)
    else : 
        with open(sys.argv[1]) as f :
            matches = f.readline().strip()
            numOfPeopleI = int(matches)

            #Read space between 
            lineSpace = f.readline()

            ## Get the preference list for all the men
            for i in range(numOfPeopleI) :
                man = []
                menchoices = f.readline().split(',')

                for j in range(len(menchoices)) :
                    man.append(int(menchoices[j]))
                #endfor

                menPrefList.append(man)
            #endfor
            
            #Read space between 
            lineSpace = f.readline()

            ## Get the preference list for all the women
            for i in range(numOfPeopleI) :
                woman = []
                womenchoices = f.readline().split(',')

                for j in range(len(womenchoices)) :
                    woman.append(int(womenchoices[j]))
                #endfor

                womenPrefList.append(woman)
            #endfor
        #endwith
    #endelse

    # Shift the numbers to index array easier
    for i in range(numOfPeopleI):
        for j in range(numOfPeopleI):
            menPrefList[i][j] = menPrefList[i][j] - 1
            womenPrefList[i][j] = womenPrefList[i][j] - 1
        #endfor
    #endfor
            
    matches = stableMatching(numOfPeopleI, menPrefList, womenPrefList)
    for i in range(len(matches)):
        matches[i][0] = matches[i][0] + 1
        matches[i][1] = matches[i][1] + 1
    #endfor

    matches.sort()
    for i in range(len(matches)):
        print(str(matches[i][0]) + ', ' + str(matches[i][1]), end="\r\n")
    #endfor
#enddef


if __name__ == '__main__' :
    main()
