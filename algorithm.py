def Backpack1(inputFile, W):
    wei = []
    val = []
    line_count = 0
    try:
        with open(inputFile, 'r') as file:
            for line in file:
                columns = line.strip().split()
                if len(columns) >= 2:
                    wei.append(int(columns[0]))
                    val.append(int(columns[1]))
                    line_count += 1
    except FileNotFoundError:
        print(f"File {file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    n = line_count
    F = Backpack1_build_solution_table(W, n, wei, val)
    total, res = Backpack1_trace_and_output_result(F, n, W, wei)
    print(f"The best fit is {total}, which are:", end=' ')
    for index in res:
        print(index, end = ' ')

def Backpack1_build_solution_table(W, n, wei, val):
    # Solution matrix comprises columns with weight from 0 to W, rows indices are numbers from 0 to n, indicate the solution
    F = [[0 for _ in range (0, W + 1)] for _ in range (0, n + 1)]
    # First row are all 0
    for i in range (1, n + 1):
        for j in range (0, W + 1):
            F[i][j] = F[i - 1][j] # Assume not pick the packback i
            if j >= wei[i - 1] and F[i][j] < F[i - 1][j - wei[i - 1]] + val[i - 1]:
                F[i][j] = F[i - 1][j - wei[i - 1]] + val[i - 1] # If picking the packback i is even better, change the option
    return F

def Backpack1_trace_and_output_result(F, n, W, wei):
    res = []
    total = F[n][W]
    while n != 0:
        if F[n][W] != F[n - 1][W]: # if an option has been picked, trace it
            res.append(n)
            W = W - wei[n - 1]
        n = n - 1
    return total, res



def FindASubSetSum_build_solution_table(s, n, sum):
    # True/False matrix comprises columns with numbers from 0 to sum, rows indices are numbers from 0 to n, indicate if 
    # the list comprises 1 to i does have subset that have sum equals j
    F = [[False for _ in range (0, sum + 1)] for _ in range (0, n + 1)]
    for i in range (1, n + 1):
        F[i][0] = True # First column is True on purpose to make all F[i][s[i]] True
        for j in range (1, sum + 1):
            if j < s[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = (F[i - 1][j] or F[i - 1][j - s[i - 1]])
    return F

def FindSubSetSum_trace_and_output_result(s, sum):
    n = len(s)
    F = FindASubSetSum_build_solution_table(s, n, sum)
    if F[n][sum] == False:
        return 0
    # for i in F:
    #     print(i)
    res = []
    i, j = n, sum
    while i > 0 and j > 0:
        if s[i - 1] <= j and F[i][j] and not F[i - 1][j]:
            res.append(i - 1)
            j -= s[i - 1]
        i -= 1
    return res

def DivideIntoTwoMostBalance(s):
    sum = 0
    for i in s:
        sum += i
    n = len(s)
    mid = sum // 2
    while(1):
        res = FindSubSetSum_trace_and_output_result(s, mid)
        if (res == 0):
            mid -= 1
        else:
            temp = []
            for i in res:
                temp.append(s.pop(i))
            return temp, s


def main():
    
    val = [5, 8, 10, 3 , 5 , 7 , 20, 50, 100, 4]
    # sum = 99
    # res = FindSubSetSum_trace_and_output_result(val, sum)
    # if res != 0:
    #     print("The subset: ", end = "")
    #     for i in res:
    #         print(val[i], end = " ")
    # else:
    #     print('No')

    # a, b = DivideIntoTwoMostBalance(val)
    # print(a)
    # print(b)
    Backpack1('input1.txt', 11)

main()