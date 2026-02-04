# Last updated: 2/4/2026, 12:16:09 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            master_dict = {}
            for word in strs:
                count_char = []
                for i in word:
                    count_char.append(i)
                count_char = sorted(count_char)
                
                if str(count_char) in master_dict:
                    master_dict[str(count_char)].append(word)
                else:
                    master_dict[str(count_char)] = [word]
        
            output_list = []
            for i in master_dict:
                output_list.append(master_dict[i])
            return output_list

   


                




        
        