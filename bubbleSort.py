# write your bubble sort algorithm below
def bubble_sort(lst):
      for i in range(len(lst)):
          iterator = 0
          swapped = False
          print(f"iteration{iterator}")
          for j in range(len(lst) - 1):
              iterator += 1
              print(f"comparing{lst[j], lst[j+1]}")
              if lst[j] > lst[j+1]:
                  lst[j], lst[j+1] = lst[j+1], lst[j]
                  swapped = True
      
          if not swapped:  
            return

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
