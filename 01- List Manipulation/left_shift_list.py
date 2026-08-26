def shift_left(lis, n):
    if not lis:
        return lis

    n = n % len(lis)
    shifted_list = lis[n:] + lis[:n]
    return shifted_list


mylist = [10, 12, 15, 17, 39, 60]
print("Original List:", mylist)
pos = int(input("Enter number of positions to shift left:"))
res = shift_left(mylist, pos)
print("List after shifting left by", pos, "positions:", res)
