def first_n_smallest(number_list, n):

    if n == 0:
        return []

    ordered_list = sorted(number_list)[:n]
    result = []

    for number in number_list:
        if number in ordered_list:
            result.append(number)
            ordered_list.remove(number)

    return result

if __name__ in '__main__':
  
  assert first_n_smallest ([1,2,3,4,5],3) == [1,2,3]
  assert first_n_smallest([5,4,3,2,1],3 )== [3,2,1] 
  assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
  assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
  assert first_n_smallest([1,2,3,4,5],0) == []
  assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
  assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
  assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
  assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
  assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]

  print("All passed")