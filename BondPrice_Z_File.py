

def getBondPrice_Z(face, couponRate, times, yc):
    
    pvm = 0
    cf = 0
    pvcf = 0
    pvcfsum = 0
    
    for i in range(0,5):
        pvm = (1+yc[i])**(-(times[i]))
        cf = face*couponRate
        if i == 4:
            cf = cf + face
        pvcf = pvm*cf
        pvcfsum = pvcfsum + pvcf
   
    return(pvcfsum)
    
    
    
   
