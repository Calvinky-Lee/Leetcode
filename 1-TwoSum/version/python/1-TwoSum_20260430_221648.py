# Last updated: 4/30/2026, 10:16:48 PM
1import copy
2class Solution:
3    def checkInclusion(self, s1: str, s2: str) -> bool:
4        s1_dict = {}
5        begin = 0
6        end = len(s1)
7        
8        for i in s1:
9            if i in s1_dict:
10                s1_dict[i] += 1
11            else:
12                s1_dict[i] = 1
13
14        while end <= len(s2):
15            counter = 0
16            temp = copy.copy(s1_dict)
17            print(temp)
18            for i in s2[begin:end]:
19                if i in s1:
20                    temp[i] -= 1
21            for key in temp:
22                if temp[key] == 0:
23                    counter += 1
24
25            if counter == len(s1_dict):
26                return True
27             
28            begin += 1
29            end += 1
30        return False
31
32
33
34
35
36            
37
38
39        