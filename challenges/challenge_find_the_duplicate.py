def find_duplicate(nums):
  for num in nums:
    try:
        if num < 0 : return False
        if ( nums.count(num) != 1): return num
    except: return False
  return False
if __name__ == '__main__':
  print(find_duplicate([1, 3, 4, 2, 2]))