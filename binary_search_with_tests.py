import unittest


class BinarySearch:
  def search_iterative(self, list, item):    
    low = 0
    high = len(list) - 1

    while low <= high:      
      mid = (low + high) // 2
      guess = list[mid]
      
      if guess == item:
        return mid
      
      if guess > item:
        high = mid - 1      
      else:
        low = mid + 1
    
    return None

  def search_recursive(self, list, low, high, item):    
    if high >= low:   
        mid = (high + low) // 2
        guess = list[mid]  
        
        if guess == item:
            return mid        
        elif guess > item: 
            return self.search_recursive(list, low, mid - 1, item)  
        else: 
            return self.search_recursive(list, mid + 1, high, item) 
    else:        
        return None


bs = BinarySearch()
simple_list = [2, 3, 4, 13, 40]


class TestBinarySearch(unittest.TestCase):
  def setUp(self):
    print ("... %s" % self._testMethodName)
  
  def test_iterative_binary_search_with_simple_list(self):    
    item, expected_index = 3, 1
    index = bs.search_iterative(simple_list, item)
    self.assertEqual(expected_index, index)

  def test_recoursive_binary_search_with_simple_list(self):
    item, expected_index = 3, 1    
    low, high = 0, len(simple_list) - 1
    index = bs.search_recursive(simple_list, low, high, item)
    self.assertEqual(expected_index, index)

  def test_search_for_nonexistent_item(self):    
    item, expected_result = 100, None
    index = bs.search_iterative(simple_list, item)
    self.assertEqual(expected_result, index)
    
    
if __name__ == '__main__':
    unittest.main()
    
