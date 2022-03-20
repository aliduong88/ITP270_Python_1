# 1. Append Size
# This code is going to calculate the length of a list and then add the length to the end of the list 
# Declare function
def append_size(lst): 
  lst.append(len(lst))
  return lst
print(append_size([23, 42, 108]))
# Answer should looks like this: [23, 42, 108, 3]

# 2. Append Sum
# This function calculates the sum of the last two elements of a list and then add the result to the list
# -1 refers to the last item in the list
# -2 refers to the second last item in the list
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst


print(append_sum([1, 1, 2]))
# Answer should looks like this: [1, 1, 2, 3, 5, 8]

# 3. Larger List
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1. 


def larger_list (lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print (larger_list ([4, 10, 2, 5], [-10, 2, 5, 10]))

# Answer should looks like this: 5

# 4. More Than N
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n (lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

print (more_than_n ([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Answer should looks like this: True

# 5. Combine Sort
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort (lst1, lst2):
  combined = sorted(lst1 + lst2)
  return combined

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Answer should looks like this: [-10, 2, 2, 4, 5, 5, 10, 10]