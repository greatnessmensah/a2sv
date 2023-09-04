def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    p_nums = [0]
    ps_nums = [0]
    q = int(input())
    ques = [list(map(int, input().split())) for _ in range(q)]
    s_nums = sorted(nums)
    
    for i in range(n):
        p_nums.append(p_nums[-1] + nums[i])
 
    for i in range(n):
        ps_nums.append(ps_nums[-1] + s_nums[i])
 
    for x in ques:
        if x[0] == 1:
            print(p_nums[x[2]]-p_nums[x[1]-1])
        else:
            print(ps_nums[x[2]]-ps_nums[x[1]-1])
 
    
if "__main__" == __name__:
    solve()
