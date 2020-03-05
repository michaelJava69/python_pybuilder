


def find_two_sum(numbers,target_sum):
    new_dict = {}
    for i , x in enumerate(numbers):
        new_dict[x] =new_dict.get(x,[])+ [i]

    print (new_dict)

    for i,x in enumerate(numbers):
        for j in new_dict.get(target_sum-x):
            print("before i = ", i, " j = ", j)

            if i<j:
                print(("number ", x, " and ", target_sum - x, " at ", i, " and ", j, " equals ", target_sum))
                #print("i = ", i, " j = ", j)








print(find_two_sum([3, 7, 5, 1, 5, 9], 10))
