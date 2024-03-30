class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nodes: list):
        self.first = ListNode(nodes[0])
        self.__latest = self.first
        for i in range(1, len(nodes)):
            self.__latest.next = ListNode(nodes[i])
            self.__latest = self.__latest.next

            
    def append(self, node):
        self.__latest.next = ListNode(node)
        self.__latest = self.__latest.next


def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    current1 = l1.first
    current2 = l2.first
    carryover = False
    digitTotal = current1.val + current2.val
    if digitTotal >= 10:
        carryover = True
        digitTotal -= 10
    final_total = LinkedList([digitTotal])

    current1 = current1.next
    current2 = current2.next
    while (not ((current1 is None) and (current2 is None))):
        digitTotal = 0
        if current1 is not None:
            digitTotal += current1.val
            current1 = current1.next
        if current2 is not None:
            digitTotal += current2.val
            current2 = current2.next
        if carryover:
            digitTotal += 1
        carryover = False
        if digitTotal >= 10:
            carryover = True
            digitTotal -= 10
        final_total.append(digitTotal)
    if carryover:
        final_total.append(1)
        
    return final_total


if __name__ == "__main__":
    test_nums = [([2,4,3],[5,6,4]),([0],[0]),
                 ([9,9,9,9,9,9,9],[9,9,9,9])]
    for num1,num2 in test_nums:
        test_total = add_two_numbers(LinkedList(num1),LinkedList(num2))
        digit = test_total.first
        list_total = []
        while (digit is not None):
            list_total.append(digit.val)
            digit = digit.next
        print(list_total)