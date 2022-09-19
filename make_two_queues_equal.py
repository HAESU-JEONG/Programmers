def solution(queue1, queue2):
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    total_length = len(queue1)
    len_queue1 = len(queue1)

    sum_total = sum_queue1 + sum_queue2
    avg = sum_total // 2

    if sum_total % 2 != 0:
        return -1

    elif max(queue1) > avg or max(queue2) > avg:
                return -1

    else:
        cnt = 0
        while True:
            if sum_queue1 == sum_queue2:
                break

            elif sum_queue1 > sum_queue2:
                if len_queue1 == 0 or len_queue1 == total_length * 2:
                    return -1

                pop_queue1 = queue1.pop(0)
                queue2.insert(len(queue2), pop_queue1)
                cnt += 1

                sum_queue1 = sum_queue1 - pop_queue1
                sum_queue2 = sum_queue2 + pop_queue1

                len_queue1 -= 1

            elif sum_queue1 < sum_queue2:
                if len_queue1 == 0 or len_queue1 == total_length * 2:
                    return -1

                pop_queue2 = queue2.pop(0)
                queue1.insert(len(queue1), pop_queue2)
                cnt += 1

                sum_queue1 = sum_queue1 + pop_queue2
                sum_queue2 = sum_queue2 - pop_queue2

                len_queue1 += 1

        return cnt
