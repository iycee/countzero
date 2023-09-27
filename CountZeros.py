def CountZeros(A):
    count = 0

    for zeros in A:
        if zeros == 0:
            count += 1

    return count


array1 = [1, 1, 1, 0, 0, 0, 5, 7]

totalzeros = CountZeros(array1)
print("there are ", totalzeros, "zeros detected")


