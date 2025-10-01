from collections import deque

def average_temp(temp_list, k=100):
    temp_q = deque(temp_list[:k], maxlen=k)

    sum_temp = sum(temp_q)
    avg_temp = [sum_temp/k]

    for next_temp in temp_list[k:]:
        sum_temp += next_temp - temp_q.popleft()
        temp_q.append(next_temp)
        avg_temp.append(sum_temp / k)

    return avg_temp