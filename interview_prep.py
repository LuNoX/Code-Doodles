import quicksort


def fizzbuzz(k):
    results = []
    for i in range(1, k+1):
        result = ''
        if i % 3 == 0:
            result += 'Fizz'
        if i % 5 == 0:
            result += 'Buzz'
        if result == '':
            results.append(i)
        else:
            results.append(result)
    return results


print(fizzbuzz(16))


def find_k_th_smallest_element(a_list, k):
    if k <= 0:
        raise Exception('k needs to be positive.')
    elif len(a_list) < k:
        raise Exception('List is smaller than k.')
    else:
        small = []
        small_filled = False
        for i in a_list:
            if small_filled:
                biggest_small = small[0]
                appended = False
                for j in small:
                    if (not appended) and i < j:
                        small.append(i)
                        appended = True
                    if j > biggest_small:
                        biggest_small = j
                if appended:
                    small.remove(biggest_small)
            else:
                small.append(i)
                if len(small) >= k:
                    small_filled = True
        result = small[0]
        for i in small:
            if i > result:
                result = i
        return result


list_to_be_used = [1, 2, 7, 10, 4, 9, 0, -2, -3]
some_k = 1

print(find_k_th_smallest_element(list_to_be_used, some_k))


def find_biggest_product(a_list):
    if len(a_list) == 0:
        return 0
    else:
        sorted__list = quicksort.sort(a_list)
        if sorted__list[-1] <= 0:
            return sorted__list[-1]
        else:
            product = 1
            biggest_negative = 1
            for i in sorted__list:
                if i != 0:
                    product = product*i
                    if i < 0 and (i > biggest_negative or biggest_negative == 1):
                        biggest_negative = i
            if product < 0:
                product = product / biggest_negative
            return product


product_list = [0, 0, -2, 4, 5, -3, -6]

print(find_biggest_product(product_list))
print(6*3*5*4)


def find_biggest_sum(a_list):
    biggest_sum = 0
    biggest_negative = 0
    contains_zero = False
    for i in a_list:
        if i > 0:
            biggest_sum += i
        elif i == 0:
            contains_zero = True
        elif contains_zero and i > biggest_negative or biggest_negative == 0:
            biggest_negative = i
    if not contains_zero and biggest_sum == 0:
        return biggest_negative
    else:
        return biggest_sum


print(find_biggest_sum([-1]))
