

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    y1 = y
    m1 = m
    pvm = 0
    cf = 0
    pvcf = 0
    pvcfsum = 0
        
    if ppy == 2:
        m1 = 2*m
        y1 = y/2
        
    for i in range(1,m1+1):
        pvm = (1+y1)**(-i)
        cf = face*couponRate/ppy
        if i == m1:
            cf = cf + face
        pvcf = cf*pvm
        pvcfsum = pvcfsum + pvcf
    
    return(pvcfsum)
