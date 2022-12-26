def printPairs(arr, arr_size, sum):
    hashmap = {}
    holder = -1
    result = []
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if temp in hashmap:
            result.append(int(arr[i]))
            result.append(int(temp))
            return result
            
        if temp > arr[arr_size - 1]:
            hashmap[arr[i]] = 1
        else:
            if holder == -1:
                holder = int(arr[i])
            hashmap[arr[i]] = 0

    result.append(holder)
    result.append(24)
    return result

def roundVolumes(inputVolume, units):
    mlList = [30, 59, 89, 118, 148, 177, 207, 237, 296, 355, 473, 532]
    ozList = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 18, 20, 24]

    unitsArr = [ozList, mlList]

    answers = []
    temporary = 0
    max = unitsArr[units][len(unitsArr[units])-1]
    
    for i in range(len(ozList)):
        if inputVolume == unitsArr[units][i]:
            answers = [unitsArr[units][i]]
            return answers

    for i in range(len(ozList)):

        if inputVolume % unitsArr[units][i] == 0:
            temporary = inputVolume / unitsArr[units][i]
            temp1 = int(temporary)
            if temporary > 4:
                continue
            else:
                for k in range(temp1):
                    answers.append(unitsArr[units][i])
            return answers
        
        elif inputVolume > max:
            answers.extend(printPairs(unitsArr[units], len(unitsArr[units]),inputVolume))
            return answers

        elif inputVolume < unitsArr[units][i]:
            if (i == 0):
                answers.append(unitsArr[units][i])
                return answers 
            else:
                average = (unitsArr[units][i] + unitsArr[units][i - 1]) / 2.0
                if (inputVolume >= average):
                    answers.append(unitsArr[units][i])
                else:
                    answers.append(unitsArr[units][i - 1])
                return answers

    return answers
