

def FizzBuzz(start, finish):
    
    myEmptyList = []
    for i in range(start,finish+1):
        if i%15 == 0:
            myEmptyList.append('fizzbuzz')
        elif i%5 == 0:
            myEmptyList.append('buzz')
        elif i%3 == 0:
            myEmptyList.append('fizz')
        else:
            myEmptyList.append(i)
         
        
    return(myEmptyList)
