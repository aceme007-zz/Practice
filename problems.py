#########################################################

# Q: check for balanced parenthesis

input = '{[<<()>>)]}['

dict = {}
correctMap = {
        "{":"}",
        "(":")",
        "[":"]",
        "<":">"
    }
invcorrectMap = {v:k for k,v in correctMap.items()}
stack = []
def isBalanced(input):
    if len(input)%2 != 0 :
        print "Not even cp1"
        return 0
    for item in input:
        if item in correctMap:
            stack.append(item)
        else:
            value = stack.pop()
            if value != invcorrectMap[item]:
                print "not bal cp2"
                return 0
    if not stack:
        print "Balanced"
        return 1
    else:
        print "Not balance cp3"
        print (stack)
        return 0
    
isBalanced(input)

#########################################################

# Q: get all sub combination of list

import itertools
s = [1,2,3,4]

def getSubLists (inputList):
    op = []
    L = len(inputList)
    for i in range(1,L+1):
        for a in itertools.combinations(inputList, i):
            op.append(a)
    return ([list(a) for a in op])

filteredSubLists = filter(lambda x: sum(x)<5, getSubLists(s))
print len(sorted(filteredSubLists, key=len)[-1])

#########################################################

# Q: get all english combinations for phone number

phoneNumber = '637'
keypadDict = {
    '1' : '',
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz',
    '0' : ''
    }
rawArray = [keypadDict[i] for i in phoneNumber]

# can be done using itertools
import itertools
for e in list(itertools.product(*rawArray)):
    print (''.join(e)),
    
def getCombo(inputList):
    L = len(inputList)
    if L == 1:
        return list(inputList[0])
    else:
        op = []
        for letter in inputList[0]:
            op = op + list(map(lambda x: x+letter, getCombo(inputList[1:])))
        return op
print(getCombo(rawArray))

#########################################################

# Q: print fibonacci numbers
a, b = 0, 1
while a < 20:
  print a,
  a, b = b, a+b
  
#########################################################

# Q: check special substring in string
def checkSpecialSubstr(string, substr):                                                                                         
    stringIndex = 0                                               
    for char in substr:                                                                                                      
        index = string[stringIndex:].find(char)                   
        if index < 0:                                             
            return False                                          
        stringIndex = stringIndex + index + 1                                                                            
    return True
print checkSpecialSubstr('abccc', 'ac')

#########################################################

# Q: how to define a class

class Animal:
  # private vars
  __name = ''
  __height = 0
  __weight = 0
  __sound = 0
  
  # encapsulation
  def set_name(self, name):
    # check if all chars
    self.__name = name
  def get_name(self):
    return self.__name
  
  def set_height(self, height):
    self.__height = height
  def get_height(self):
    return self.__height
  
  def set_weight(self, weight):
    self.__weight = weight
  def get_weight(self):
    return self.__weight

  def set_sound(self, sound):
    self.__sound = sound
  def get_sound(self):
    return self.__sound
  
  # constructor
  def __init__(self, name, height, weight, sound):
    self.__name = name
    self.__height = height
    self.__weight = weight
    self.__sound = sound
    
  def get_type(self):
    print ('Animal')
  
  def toString(self):
    return "{} is {} cm tall, weighs {} kg and speaks {}".format(self.__name, self.__height, self.__weight, self.__sound)
   
  
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString)

# inheritance

class Dog(Animal):
  __owner = ''
  
  def __init__(self, name, height, weight, sound, owner):
    self.__owner = owner
    Animal.__init__(self, name, height, weight, sound)
    
  def set_owner(self, owner):
    self.__owner = owner
  def get_owner(self):
    return self.__owner
  
  def get_type(self):
    print ("Dog")
  
  def toString(self):
    return "{} is {} cm tall, weighs {} kg and speaks {}. His owner is {}".format(
      self.__name, self.__height, self.__weight, self.__sound, self.__owner)
  
  def multiple_sounds(self, howMany=None):
    if howMany is None:
      print (self.get_sound)
    else:
      print (self.get_sound()*howMany)
  
spot = Dog ('Spot', 53, 23, 'Ruff', 'kaul')

#########################################################

# Q: sliding window returns sum of k elements 
"""Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6
"""

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3

op = []
def getArray(arr, k):
    for i in range(len(arr)+1-k):
        op.append(max(arr[i:k+i]))
    return op

print(getArray(arr, k))

#########################################################

# Q: jumping numbers

# get jumping numbers till N
# 0 1 2 3 4 5 6 7 8 9 10 12 21 23

def isdiffOne(x):
    for i in range(len(x)-1):
        if abs(int(x[i])-int(x[i+1])) != 1:
            return 0
    return 1
        
op = []
def getJP(N):
    for i in range(N+1):
        if i < 11: 
            op.append(i)
        else:
            if isdiffOne(str(i)):
                op.append(i)
    return op

print(getJP(67))
    
#########################################################

# Q: fizzbuzz problem
def getFizzBuzz(N):
    for i in range(1, N+1):
        if i%5 == 0:
            x = "Buzz"
        elif i%3 == 0:
            x = "Fizz"
        else:
            x = i
        if i%3 == 0 and i%5 == 0:
            x = "FizzBuzz"        
        op.append(x)
        print (i, x)
op = []    
getFizzBuzz(100)

#########################################################

# Q: print range when given sorted list of num
M = [2,3,4,5,10,18,19,20]
# [2-5,10,18-20]

op = []
def getLastcontinuousSubArrayIndex(arr):
    # returns index uptil continous subarray
    L = len(arr)
    start = arr[0]
    if L == 1:
        return 0
    else:
        for i in range(1, L):
            if arr[i] == start+1:
                start += 1
            else:
                return i-1
        return L-1
              
def getArrayRange(N):
    L = len(N)
    if L <= 1:
        return
    endIndex = 0
    startIndex = 0
    # make sure M is sorted
    while len(N) > 1:
        endIndex = getLastcontinuousSubArrayIndex(N)
        if startIndex != endIndex:
            tempStr = str(N[startIndex]) + "-" + str(N[endIndex])
            op.append(tempStr)
        else:
            op.append(N[startIndex])
        N = N[endIndex+1:]    
        startIndex = 0
    
getArrayRange(M)
print(op)

#########################################################

# Q: fibonacci with dynamic prog
t1, t2, n = 0, 1, 6

dict = {}
dict[1] = t1
dict[2] = t2 

def fibo(n):   
    if n in dict:
        return dict[n]
    op = fibo(n-2) + fibo(n-1)**2
    dict[n] = op
    return op
    
print(fibo(n))

#########################################################

# Q: x,y->x+y,y or x,y+x problem
# x, y -> x+y, y
# x, y -> x, y+x

def newList (listTuples):
    op1 = []
    for eachTuple in listTuples:
        op1 += combo(eachTuple[0], eachTuple[1])
    return op1
        
def combo (x,y):
    return [(x+y,y), (x,y+x)]

def isPossible(a, b, c, d):
    output = (c, d)
    op = combo(a,b)
    while 1:
        op = newList (op)
        if output in op:
            print ("Yes")
            return
        for et in op:
            if et < output:
                # this means it can still match
                pass
            else:
                print ("No")
                return
    
isPossible(1, 2, 3, 6)
isPossible(1, 4, 5, 9)

#########################################################

# KADANE ALGO
# Q: max subarray sum contiguous kadane algo
#A = [1, -3, 5, -2, 9, -8, -6, 4]
A = [-2, 3, 2, -1]

def maxSum(A):
  current_max = A[0]
  global_max = A[0]
  for i in range(1, len(A)-1):
    curent_max = max(A[i], current_max + A[i])
    if current_max > global_max:
      global_max = current_max
  return global_max

#########################################################

# Q: longest palindrome substring manacher algo
# MANACHER ALGO

def getLongestPalin(A):
    L = len(A)
    currentLong = ''
    maxLen = 0
    palin = []
    # get all 1 chars
    for i in range(L):
        palin.append(A[i])
        currentLong = A[i]
        maxLen = 1
    # get all 2 chars
    for i in range(L-1):
        newStr = A[i:i+2]
        if newStr == newStr[::-1]:
            currentLong = newStr
            palin.append(newStr)
            maxLen = 2
    print(palin)
    # loop around now for rest
    for length in range(3, L):
        for i in range(L-length+1):
            j = i+length-1
            if A[i] == A[j] and A[i+1:j] in palin:
                palin.append(A[i:j+1])
    
    print (palin[-1])

#A = 'nnbanana'
A = 'nitinmamamni'
getLongestPalin(A)

#########################################################

# Q: simple binary search
# takes O(logn) time vs O(N)

def BS(A, x):
    low = 0
    high = len(A)-1
    while low < high:
        mid = int(low + ((high-low)/2))
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return -1

      
L = [2,4,7,9,11,13,15,17,55,77,99]
print(BS(L,15))

#########################################################

# Q: tower of hanoi

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print (source, helper, target)

#########################################################

# Q: location of a value in rotated array

A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

def helper(arr, low, high, value):
    while low <= high:
        mid = int((low+high)/2)
        # check if we found it
        if arr[mid] == value:
            return mid
        elif arr[low] <= arr[mid]:
            # check between low to mid
            if value > arr[mid]:
                low = mid+1
            elif value >= arr[low]:
                high = mid-1
            else:
                low = mid+1
        elif value <= arr[high]:
            low = mid+1
        elif value < arr[mid]:
            high = mid-1
        else:
            high = mid-1
    return -1

def locateValue(arr, value):
    L = len(arr)
    return (helper(arr, 0, L-1, value))

print(locateValue(A,5))

#########################################################

# Q: Level Order Traversal (BFS/DFS)

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    
class Solution:
  def insert(self, root, data):
    if root == None:
      return Node(data)
    else:
      if data <= root.left:
        curr = self.insert(root.left, data)
        root.left = curr
      else:
        curr = self.insert(root.right, data)
        root.right = curr
    return root
  
  def levelOrder(self, root):
    Q = []
    if root == None:
      return
    else:
      Q.append(root)
      while Q:
        curr = Q[0]
        print (curr.data)
        if curr.left != None:
          Q.append(curr.left)
        if curr.right != None:
          Q.append(curr.right)
        Q.pop(0)
    
myTree = Solution()
root = None
data = [3, 5, 4, 7, 2, 1]
root = myTree.insert(root, data)
myTree.levelOrder(root)

#########################################################

# Q: Restaurant total bill using class

class Bill:
    def __init__(self, total, tip, tax):
        self.total = float(total)
        self.tip = tip
        self.tax = tax
        
    def CalculateTip(self):
        return float((self.total * self.tip) / 100)
        
    def CalculateTax(self):
        return float((self.total * self.tax) / 100)
        
    def FinalBill(self):
        sum = self.total
        sum += self.CalculateTip()
        sum += self.CalculateTax()
        return int(round(sum))

total = float(input())
tip = int(input())
tax = int(input())
      
newBill = Bill(total, tip, tax)
f = newBill.FinalBill()
print("The total meal cost is "+str(f)+" dollars.")

#########################################################

# Q: Person age using class

class MyPerson:
  def __init__(self, age):
    if age > 0:
      self.age = age
    else:
      self.age = 0
      print ("Age is not valid, setting age to 0.")
  
  def yearPasses(self):
    self.age += 1
    
  def amIOld(self):
    if self.age < 13:
      print ("You are young.")
    elif self.age >= 13 and self.age < 18:
      print ("You are a teenager.")
    else:
      print ("You are old.")
  

P1 = MyPerson(-1)
P1.amIOld()
for j in range(0,3):
  P1.yearPasses()
P1.amIOld()

#########################################################

# Q: Inheritance person student

class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber
    
  def Print(self):
    print("Name:", self.lastName + ',', self.firstName)
    print("ID:", self.idNumber)
  
  
class Student(Person):
  def __init__(self, firstName, lastName, i_d, scores):
    self.scores = scores
    Person.__init__(self, firstName, lastName, i_d)
    
  def calculate(self):
    arr = self.scores
    avg = int(sum(arr)/len(arr))
    if avg >= 90 and avg <= 100:
      return 'O'
    elif avg >= 80 and avg < 90:
      return 'E'
    elif avg >= 70 and avg < 80:
      return 'A'
    elif avg >= 55 and avg < 70:
      return 'P'
    elif avg >= 40 and avg < 55:
      return 'D'
    else:
      return 'T'
    
    
#########################################################

# Q: Linked List

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Solution:
  def display(self, head):
    curr = head
    while curr:
      print (curr.data, )
      curr = curr.next
     
  def insert(self, head, data):
    newNode = Node(data)
    if head == None:
      head = newNode
      return head
    curr = head
    while curr:
      curr = curr.next
    curr.next = newNode
    return head
      
 #########################################################

# Q: Calculator class with exception

class Calculator:
  
  def power(self, n, p):
    if n < 0 or p < 0:
      raise Exception("n and p should be non-negative")
    else:
      return (n**p)
  
#########################################################

# Q: Binary Tree Insert Traverse InOrder LDR

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BT:
    def insert(self, root, data):
        newNode = Node(data)
        if root == None:
            root = newNode
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root
    def printArray(self, root):
        if root == None:
            return
        self.printArray(root.left)
        print(root.data)
        self.printArray(root.right)

    
newBT = BT()
root = None
root = newBT.insert(root, 5)
root = newBT.insert(root, 67)
root = newBT.insert(root, 1)
root = newBT.insert(root, 30)
root = newBT.insert(root, 42)
root = newBT.insert(root, 92)
root = newBT.insert(root, 4)
newBT.printArray(root)

#########################################################

# Q: coin change problem

def coin_change(n, coins, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins == []:
        pass
    else:
        for c in coin_change(n, coins[:], coins_so_far+[coins[0]]):
            yield c
        for c in coin_change(n, coins[1:], coins_so_far):
            yield c
            

n = 7
coins = [1, 5, 10, 15]
sol = [s for s in coin_change(n, coins, [])]

#########################################################

# Q:










#########################################################
