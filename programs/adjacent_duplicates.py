class Solution(object):
   def removeDuplicates(self, S):
      st = []
      i = 0
      while i < len(S):
         if len(st)!=0 and st[-1]==S[i]:
            i+=1
            st.pop(-1)
         else:
            st.append(S[i])
            i+=1
      return "".join(i for i in st)
ob1 = Solution()
a=input("enter a string :")
print(ob1.removeDuplicates(a))