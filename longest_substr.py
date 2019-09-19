class MyDictionary(dict):
    def __init__(self):
        self = dict()
        
    def add(self, key, value):
        self[key] = value
    
    def _flush(self):
        self.clear()
        
    def getVal(self, key):
        return self.get(key)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_obj = MyDictionary()
        store_size = []
        lenofstr = len(s)
        final_high = local_cur_high = cur_high = 0 
        index_value = 0
        for i in range(0, lenofstr):
            if i == 0:
                dict_obj.add(hash(s[i]), i)
                store_size.append(len(dict_obj))
            else:
                temp_hash = hash(s[i])
                if temp_hash not in dict_obj:
                    dict_obj.add(hash(s[i]), i)
                    #local_cur_high = len(dict_obj)
                    store_size.append(len(dict_obj))
                else:
                    index_value = dict_obj.getVal(hash(s[i])) + 1
                    now_index = i
                    store_size.append(len(dict_obj))
                    dict_obj._flush()
                    for x in range(index_value, now_index + 1):
                        dict_obj.add(hash(s[x]), x)
        store_size.sort(reverse = True)
        try:
            cur_high = store_size.pop(0)
        except IndexError:
            cur_high = 0
        return cur_high