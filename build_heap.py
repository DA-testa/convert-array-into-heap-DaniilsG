def heapify(data, n, i, swaps):
    
    
    smallest = i 
     
    left = 2 * i + 1   
     
    right = 2 * i + 2     

    if left < n and data[i] > data[left]:
        smallest = left

    if right < n and data[smallest] > data[right]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, n, smallest, swaps)


def build_heap(data, n):
    swaps = []

    for i in range(n // 2, -1, -1):
        heapify(data, n, i, swaps)

    return swaps


def main():
    
    try:
        text = input("I vai F: ")
        
        if text.startswith('I'):
            n = int(input("cipars: "))
            data = list(map(int, input().split()))
            
        elif text.startswith('F'):
            
            filename = "tests/" + input("Fails: ")
            
            with open(filename, "r") as file:
                
                n = int(file.readline())
                data = list(map(int, file.readline().split()))

        assert len(data) == n

        swaps = build_heap(data, n)

        print(len(swaps))
        
        for i, j in swaps:
            print(i, j)
            
    except Exception as e:
        
        print(f"Error: {e}")
        return


if __name__ == "main":
    main()