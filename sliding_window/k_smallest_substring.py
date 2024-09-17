def k_smallest_substring(input_str, k):
    n = len(input_str)
    start, count = 0, 0
    min_string = input_str
    for end in range(n):
        if input_str[end] == "1":
            count+=1
        while count == k:
            current_string = input_str[start:end+1]
            if len(min_string)>len(current_string):
                min_string = current_string
            if len(min_string) == len(current_string) and min_string>current_string:
                min_string = current_string
            if input_str[start] == "1":
                count-=1
            start+=1
    return min_string

input_str = "0101101"
k=3
result = k_smallest_substring(input_str, k)
print(result)
    