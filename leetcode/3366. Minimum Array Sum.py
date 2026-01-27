import math

class Solution:
    def minArraySum(self, nums, k, op1, op2):
        n = len(nums)
        # Инициализируем таблицу бесконечностью
        # dp[i][j][k] - мин. сумма первых i чисел, потратив j раз op1 и k раз op2
        dp = [[[float('inf')] * (op2 + 1) for _ in range(op1 + 1)] for _ in range(n + 1)]
        
        # Базовое состояние: для 0 чисел сумма 0
        dp[0][0][0] = 0
        
        for i in range(n):
            x = nums[i]
            # Вычисляем возможные значения после операций заранее
            v_none = x
            v_op1 = (x + 1) // 2
            v_op2 = x - k if x >= k else float('inf')
            
            # Обе операции: сначала 1 потом 2
            v_op1_2 = v_op1 - k if v_op1 >= k else float('inf')
            # Обе операции: сначала 2 потом 1
            v_op2_1 = (v_op2 + 1) // 2 if v_op2 != float('inf') else float('inf')
            
            # Берем минимальное из двух порядков применения
            v_both = min(v_op1_2, v_op2_1)
            
            for j in range(op1 + 1):
                for l in range(op2 + 1):
                    if dp[i][j][l] == float('inf'):
                        continue
                    
                    curr_sum = dp[i][j][l]
                    
                    # 1. Ничего не применяем
                    dp[i+1][j][l] = min(dp[i+1][j][l], curr_sum + v_none)
                    
                    # 2. Применяем только Operation 1
                    if j + 1 <= op1:
                        dp[i+1][j+1][l] = min(dp[i+1][j+1][l], curr_sum + v_op1)
                    
                    # 3. Применяем только Operation 2
                    if l + 1 <= op2 and v_op2 != float('inf'):
                        dp[i+1][j][l+1] = min(dp[i+1][j][l+1], curr_sum + v_op2)
                        
                    # 4. Применяем обе операции
                    if j + 1 <= op1 and l + 1 <= op2 and v_both != float('inf'):
                        dp[i+1][j+1][l+1] = min(dp[i+1][j+1][l+1], curr_sum + v_both)
        
        # Итоговый ответ — минимум в последнем слое (для n элементов)
        ans = float('inf')
        for j in range(op1 + 1):
            for l in range(op2 + 1):
                ans = min(ans, dp[n][j][l])
        
        return ans

        

        


print(Solution().minArraySum(nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1))