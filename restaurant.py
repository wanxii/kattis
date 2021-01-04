import sys


def is_different_order(order_list, menu, index1, index2, cost):
    order1 = trace_order(order_list, menu, index1, cost)
    order2 = trace_order(order_list, menu, index2, cost)
    if order1 == order2:
        return False
    return True


def trace_order(order_list, menu, last_index, cost):
    rv = []
    if last_index == -1:
        return [cost]
    while cost > 0:
        if type(last_index) == str:
            return last_index
        rv.append(last_index + 1)
        cost -= menu[last_index]
        last_index = order_list[cost]
    return sorted(rv)


def compute_order_list(orders, menu, n):
    lst = [None for _ in range(max(orders) + 1)]
    lst[0] = -1

    for cost in range(1, len(lst)):
        for i in range(n):

            if cost < min(menu):
                lst[cost] = 'Impossible'
                break

            if cost - menu[i] >= 0:
                order = lst[cost - menu[i]]

                if type(order) == int:
                    if type(lst[cost]) == int:
                        if is_different_order(lst, menu, lst[cost], order, cost):
                            lst[cost] = 'Ambiguous'
                            break
                    else:
                        lst[cost] = i

                elif order == 'Ambiguous':
                    lst[cost] = order
                    break

                else:
                    if type(lst[cost]) != int:
                        lst[cost] = order

    return lst


def main(input):
    n = int(input.readline())
    assert 1 <= n <= 100, 'Number of items out of range'

    menu = [int(cost) for cost in input.readline().split()]
    assert len(menu) == n, 'Number of items unmatched'
    assert max(menu) <= 1000, 'No item costs more than 1000 SEK'

    m = int(input.readline())
    assert 1 <= m <= 1000

    orders = [int(order) for order in input.readline().split()]
    assert len(orders) == m, 'Number of orders unmatched'
    assert 1 <= max(orders) <= 30000, 'Total cost of some orders out of range'

    lst = compute_order_list(orders, menu, n)
    for cost in orders:
        order = lst[cost]
        if type(order) == int:
            rv = trace_order(lst, menu, order, cost)
            print(*rv)
        else: 
            print(order)


if __name__ == '__main__':
    main(sys.stdin)