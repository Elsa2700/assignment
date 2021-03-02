#====================================================================
# 一、完成以下函式，在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和。
#====================================================================
def calculate(min, max):
    sum=0
    for i in range(min,(max+1)):
        sum+=i
    print(sum)
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#====================================================================
# 二、完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
#====================================================================

#無限參數的設定(*參數)
def avg(data):
    sum=0
    total=len(data["employees"])
    for i in range(0,total):
        sum+=data["employees"][i]['salary']
    print("員工的平均薪資:",sum/total)
    
# 請用你的程式補完這個函式的區塊
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

#====================================================================
# 三、找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
#====================================================================

def maxProduct(nums):
    value=[]
    for i in range(0,(len(nums)-1)):
        for ii in range((i+1),(len(nums))):
            prod=nums[i]*nums[(ii)]
            value+=[prod]
            # print(nums[i],"x",nums[ii],"=",nums[i]*nums[ii])
    print("兩兩相乘最大值為:",max(value))

# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

#====================================================================
# 四、Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.
#====================================================================
def twoSum(nums, target):
    for i in range(0,len(nums)-1):
        for ii in range(i+1, len(nums)):
            twoSum=nums[i]+nums[ii]
            if nums[i]+nums[ii]==target:
                return [i,ii]
# # your code here
result=twoSum([2, 11, 7, 15], 9)
print(result)

#====================================================================
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。
#====================================================================

def maxZeros(nums):
    #建立alllenZero空資料:裝每個索引的後面總共有多少個0相接
    alllenZero=[0]
    #第一輪迴圈:跑每一筆索引
    for i in range(1,len(nums)):
        #第一個判斷式:判斷索引是否本身為0:
        if nums[i-1]==0:
            # 索引本身為0，計算該索引後面有多少個0
            #建立lenZero空資料，用來數該索引後面0的長度
            lenZero=0
            for ii in range((i-1),(len(nums)-1)): 
                #第二個判斷式:判斷索引後面是否有1:
                if nums[ii+1]==1:
                    #後面有1，停止計算
                    break              
                else:
                    #後面沒有1，lenZero加一個單位       
                    lenZero+=1
            #將每個本身為0的索引，其個別有多少個連續0，裝在一起，以便於最後找出連續最長的0
            alllenZero+=[lenZero+1]  
        # 索引本身不為0，直接跳過，跑下一個     
        else:
            continue
    print(max(alllenZero))
# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0






    

    

    



