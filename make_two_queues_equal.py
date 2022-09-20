from collections import deque

def solution(queue1, queue2):
    deq_queue1 = deque(queue1) # convert list to deque
    deq_queue2 = deque(queue2) # convert list to deque

    sum_queue1 = sum(deq_queue1)
    sum_queue2 = sum(deq_queue2)

    sum_total = sum(deq_queue1) + sum(deq_queue2)

    if sum_total % 2 != 0: # if sum_total is odd => cannot equal the sum of each queue
        return -1

    else:
        for cnt in range(len(deq_queue1) * 3):
            if sum_queue1 == sum_queue2:
                return cnt

            if sum_queue1 > sum_queue2:
                pop_queue1 = deq_queue1.popleft()
                deq_queue2.append(pop_queue1)
                sum_queue1 -= pop_queue1
                sum_queue2 += pop_queue1

            else:
                pop_queue2 = deq_queue2.popleft()
                deq_queue1.append(pop_queue2)
                sum_queue1 += pop_queue2
                sum_queue2 -= pop_queue2
        
        return -1