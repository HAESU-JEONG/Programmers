def solution(queue1, queue2):
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    sum_total = sum_queue1 + sum_queue2

    if sum_total % 2 != 0:
        return -1
    else:
        cnt = 0
        while True:
            if sum_queue1 == sum_queue2:
                break

            elif sum_queue1 > sum_queue2:
                pop_queue1 = queue1.pop()
                queue2.insert(pop_queue1)
                cnt += 1

            elif sum_queue1 < sum_queue2:
                pop_queue2 = queue2.pop()
                queue1.insert(pop_queue2)
                cnt += 1
            
            sum_queue1 = sum(queue1)
            sum_queue2 = sum(queue2)

        return cnt
