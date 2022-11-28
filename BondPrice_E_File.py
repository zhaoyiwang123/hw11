

def getBondPrice_E(face, couponRate, yc):
    
    t = [1,2,3,4,5]
    pvm = 0
    cf = 0
    pvcf = 0
    pvcfsum = 0
    
    for i in t:
        pvm = (1+yc[i-1])**(-i)
        cf = face*couponRate
        if i == 5:
            cf = cf + face
        pvcf = pvm*cf
        pvcfsum = pvcfsum + pvcf
   
    return(pvcfsum)
