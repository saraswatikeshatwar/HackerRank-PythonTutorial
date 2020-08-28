if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #convert to list
    arr = list(set(list(arr)))
    #store length
    ar = len(arr)
    #sort the array
    arr = sorted(arr)
    #print last second number as ruuner up score
    print(arr[ar-2])
