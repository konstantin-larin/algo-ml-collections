class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = [[1]]
        for i in range(1, numRows):
            top_arr = arr[i - 1]
            sub_arr = []
            for j in range(i):                
                if j == 0:
                    sub_arr.append(top_arr[j])
                if j == i - 1:
                    sub_arr.append(top_arr[j])
                else:
                    sub_arr.append(top_arr[j] + top_arr[j + 1])
            arr.append(sub_arr)
        return arr

            
