#!/usr/bin/python3
import unittest
import random

Reference = lambda SZ_REF: [random.randint(1,2<<16) for i in range(SZ_REF)]

DEFAULT_CACHE = 7
cache_base = 0
cache = []

# cache2ref = lambda ci, reference: (ci+len(reference))%len(reference)
def zero2ref(i, reference):
    offset = -(len(cache) // 2)+i
    ri_raw = cache_base + offset
    return (ri_raw+len(reference))%len(reference)
    # print('>>>',i,ci)
    # return cache2ref(cache_base+ci, reference)
    
def init_cache(reference):
    global cache
    if len(reference)<DEFAULT_CACHE:
        cache = [reference[zero2ref(i, reference)] for i in range(len(reference))]
    else:
        cache = [reference[zero2ref(i, reference)] for i in range(DEFAULT_CACHE)]
    
def forward_cache(reference):
    global cache
    global cache_base
    cache_base += 1
    if cache_base >= len(reference):
        cache_base = 0
    cache = cache[1:] + [reference[zero2ref(len(cache)-1, reference)]]

def backward_cache(reference):
    global cache
    global cache_base
    cache_base -= 1
    if cache_base < 0:
        cache_base = len(reference)-1
    cache = [reference[zero2ref(0, reference)]] + cache[:-1]

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        global cache, cache_base
        cache_base = 0
        cache = []

    # def test_ref30(self):
    #     reference = Reference(30)
    #     init_cache(reference)
    #     self.assertEqual(len(cache), DEFAULT_CACHE)
        
    # def test_ref30_forward(self):
    #     reference = Reference(30)
    #     init_cache(reference)
    #     for i in range(len(reference)):
    #         forward_cache(reference)
            
    # def test_ref30_backward(self):
    #     reference = Reference(30)
    #     init_cache(reference)
    #     for i in range(len(reference)):
    #         backward_cache(reference)
        
    # def test_ref3(self):
    #     reference = Reference(3)
    #     init_cache(reference)
    #     self.assertEqual(len(cache), len(reference))
        
    # def test_ref3_forward(self):
    #     reference = Reference(3)
    #     init_cache(reference)
    #     for i in range(len(reference)):
    #         forward_cache(reference)
            
    # def test_ref3_backward(self):
    #     reference = Reference(3)
    #     init_cache(reference)
    #     for i in range(len(reference)):
    #         backward_cache(reference)
            
    # def test_refgen_forward(self):
    #     reference = [3,4,9,6,1,2,0,7,5]
        
    #     init_cache(reference)
    #     print(cache)
    #     self.assertEqual(''.join(str(i) for i in cache), '3496120')
    #     forward_cache(reference)
    #     self.assertEqual(''.join(str(i) for i in cache), '4961207')
    #     # forward_cache(reference)
    #     # self.assertEqual(''.join(str(i) for i in cache), '5349612')
    #     # forward_cache(reference)
    #     # self.assertEqual(''.join(str(i) for i in cache), '3496120')
            
    # def test_refinit(self):
    #     reference = [3,4,9,6,1,2,0,7,5]
    #     init_cache(reference)
    #     self.assertEqual(''.join(str(i) for i in cache), '3496120')
        
    def test_refaddr(self):
        reference = [3,4,9,6,1,2,0,7,5]
        init_cache(reference)
        reference_indices = [zero2ref(i, reference) for i in range(6)]
        self.assertEqual(''.join(str(i) for i in reference_indices), '678012')
        
        # TODO shift cache_base 
        

if __name__ == '__main__':
    unittest.main()
    
