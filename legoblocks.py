first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

def legoBlocks(n, m):
    numbers = [1,2,3,4]
    
    def case(n, m, numbers):
        dp = [0] * (m+1)
        dp[0] = 1
        for i in range(1, m+1):
            for j in numbers:
                if i >= j:
                    dp[i] = dp[i] + dp[i-j]
        return dp[m] ** n

    total_case = case(n, m, numbers)
    #print("total_case:", total_case)
    
    delete_case= 0
    for i in range(1, m):
        left_case = case(n, i, numbers)
        right_case = case(n, m-i, numbers)
        print("left:", left_case, "///", "right:", right_case)
        delete_case += right_case * left_case

    return total_case - delete_case


legoBlocks(n,m)