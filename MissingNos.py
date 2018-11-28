def missing_numbers(num_list):
      firstnum_list = [a for a in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(firstnum_list)))

print(missing_numbers([0,1,2,3,4,6,7,10,12,14,16,20]))
