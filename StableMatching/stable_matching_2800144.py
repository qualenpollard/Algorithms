import sys

def preferenceCheck(numPeople, preferenceList, womanI, manI, currentPartnerI) :
    '''
    This method checks the preference of the current woman chosen to see if she'd rather be with
    her current partner or with the new partner.
    '''
    for i in range(numPeople) :
        if(preferenceList[womanI][i] == currentPartnerI) :
            return 1
        
        if(preferenceList[womanI][i] == manI) :
            return 0

    
def stableMatching(numMenWomenI, menPrefList, womenPrefList) :
    '''
    This function recieves the number of matches to be made, as well as the preference of each man and woman.
    It goes through each man checks the preference, and engages the two if the woman isn't already engaged.
    If the woman is engaged, it checks her preferences to see if she'd rather be with her current partner
        or with the man that seeks to be with her.
    Engaged is a List of Lists. Each list in engaged will hold the engaged couple.

    The values are shifted down by one for easy indexing in the menPrefList and womenPrefList.
    '''
    ## Number of free people
    freeCount = numMenWomenI

    ## Stores partner of women.
    wPartner = [None] * numMenWomenI
    
    ## Stores availability of men.
    mFree = [None] * numMenWomenI

    ## Stores engaged pairs
    engaged = []
    
    while(freeCount > 0) :

        ## Get the first free man
        for m in range(numMenWomenI) :
            if(mFree[m] == None) :
                break
        
        ## Go through m's preferences
        for i in range(numMenWomenI) :
            if (mFree[m] != None) :
                break
            
            ## Highest-ranked in m's preferences
            w = menPrefList[m][i]

            ## If w is free, engage(m, w)
            if(wPartner[w-(numMenWomenI)] == None) :
                wPartner[w-(numMenWomenI)] = m 
                mFree[m] = w
                engaged.append([m, w])
                freeCount = freeCount - 1
            else :
                m1 = wPartner[w-(numMenWomenI)]

                if(preferenceCheck(numMenWomenI, womenPrefList, w, m, m1) == 0) :
                    wPartner[w-(numMenWomenI)] = m 
                    mFree[m] = w
                    mFree[m1] = None
                    engaged.append([m, w])
                    engaged.remove(engaged[m1])
    
    
    for i in range(numMenWomenI) :
        engaged[i][0] = engaged[i][0] + 1
        engaged[i][1] = engaged[i][1] + 1

    engaged.sort()
    return (engaged)

def main() :
    menPrefList = []
    womenPrefList = []

    if len(sys.argv) < 2 :
        print('error: incorrect format')
        print('Try: python stable_matching_2800144.py inputfile.txt')
        sys.exit(0)
    else : 
        with open(sys.argv[1]) as f :
            slurp = f.read(2)
            if(slurp[1].isdigit()) :
                numOfPeopleI = int(slurp)
                slurp = f.read()
                #print('if')
                slurp = slurp.replace('\r\n','')
                slurp = slurp.replace(',', '')
                #print(slurp)
            else :
                numOfPeopleI = int(slurp[0])
                slurp = f.read()
                slurp = slurp.replace('\r\n', '')
                slurp = slurp.replace(',', '')
                slurp = slurp[1:len(slurp)]

        ## Get the preference list for all the men
        for i in range(numOfPeopleI) :
            man = []

            for j in range(numOfPeopleI) :
                man.append(int(slurp[0]) - 1)
                slurp = slurp[1:]
            
            
            menPrefList.append(man)
        
        ## Get the preference list for all the women
        for i in range(numOfPeopleI) :
            woman = []

            for j in range(numOfPeopleI) :
                woman.append(int(slurp[0]) - 1)
                slurp = slurp[1:]

            womenPrefList.append(woman)
            
    matches = stableMatching(numOfPeopleI, menPrefList, womenPrefList)
    print(matches)


if __name__ == '__main__' :
    main()
