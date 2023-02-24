'''
The idea is to start from the right of the input data n and find the increasing
 sequence one by one, and then store that sequence in the list and delete the
 loop in n, and then divide n into increasing sequences, and then find the KTH
 sequence from the list and find its first digit
解题思路是从输入数据n的右边开始逐个找出递增序列，然后把这个序列存进列表并在n中删除
循环这个步骤，就可以把n分成几个递增序列，之后再从列表中找到第k个序列并求他的首位数字
'''
def get_k_run_starter(n, k):
    def length(x):
        i=0
        while x!=0:
            x=x//10
            i+=1
        return i
    #Define a function to find the length of an int, which is used in the last step
    #定义一个函数用来求一个int数据的长度，最后一步才用到这个函数
    final=None
    #Use final as the final return value, and the initial value is None
    #用final作为最后的返回值，定初值为None
    num2=n
    #num2 is used to count the number of digits left in n each time an increment is removed from the right of n. The initial value is n
    #num2是用来统计每次从n右边开始删掉一个递增数据后n剩余的数字，初始值是n
    #For example, n is 123444345 and 123444 is deleted once
    #例如n为123444345删掉一次后为123444
    my_list=[]
    #The list of all increasing sequences used to hold n
    #用来存放n这个数据的所有递增序列的列表
    '''
    The way to split it is to determine whether the number on the right is 
    larger than the number on the left. If it is, let i increment, and when 
    the loop condition is not satisfied, use n% (10**i) to get the first 
    increasing sequence from the right of n, and then add it to the list, 
    Also use the variable num2 to record n// (10**i) to get the remaining number 
    after removing n from the right side of the increasing sequence. Repeat 
    this operation to get the entire increasing sequence
    '''
    '''
    拆分方法是判断右边数字是否比左边数字大如果是，就让i变量自增，当这个循环条件不满足之后
    用n%（10**i）就可以得到从n右边开始的第一个递增序列，然后把他加进列表，同时用变量num2
    来记录n//（10**i）得到把n从右边去掉此递增序列后的剩余数字，重复进行此操作以获得全部递
    增序列
    '''
    while n!=0:
        i=1
        #The i here is the first increasing sequence from the right to the left of the input int data n (this sequence subscript 0)
        #这里的i是用来统计输入的int数据n从右边开始往左数的第一个递增序列（此序列下标0）
        while n % 10 > n % 100 // 10:
            #Determine if the number on the right is larger than the number on the left
            #判断右边数字是否比左边数字大
            i+=1
            n=n//10
            #Each loop removes one digit from n
            #每循环一次就让n的数字删除一位
        my_list.append(num2 % (10 ** i))
        num2=num2//(10**i)
        #num2 % (10**i) yields an increasing sequence, and num2//(10**i) yields the remaining data after removing the increasing sequence
        #num2 % (10 ** i)得到的是递增序列，num2//(10**i)得到的是去掉递增序列后的剩余数据
        n=n//10
        '''
        i'm going to make n//10 again because the loop has been executed twice
        , which means n//10 has been executed twice, but I is already 3, 
        so //10 is needed again to match the digits that have just been removed
         from the incrementing sequence. n is confused with num2, which is to 
         allow the loop to continue, and num2 is to extract the incrementing sequence
        '''
        #在这里让n再次//10是因为循环执行了两次，意味着n//10了两次，但是i的值已经是3，所以
        #要再次//10来让数位匹配到刚删除完递增序列后的数字
        #这里的n和num2容易混淆，n的作用是让循环可以继续下去，num2则是用来提取递增序列
    print(my_list)
    final=my_list[k]//(10**(length(my_list[k])-1))
    #my_list[k] is the increasing sequence required, its length determined by the length function defined at the beginning
    #my_list[k]就是要求的那个递增序列，用开始定义的length函数求他的长度，
    # my_list[k]//(10**(length(my_list[k])-1))求首位数字
    return final
print(get_k_run_starter(123444345,0))
