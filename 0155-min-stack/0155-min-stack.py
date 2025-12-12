class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# class MinStack:

# #     def __init__(self):
# #         self.stack=[]
# #         self.min=[]

# #     def push(self, val: int) -> None:
# #         self.stack.append(val)
# #         val=min(val,self.min[-1] if self.min else val)
# #         self.min.append(val)
        

# #     def pop(self) -> None:
# #         self.stack.pop()
# #         self.min.pop()
        

# #     def top(self) -> int:
# #         return self.stack[-1]
        

# #     def getMin(self) -> int:
# #         return self.min[-1]


# # # Your MinStack object will be instantiated and called as such:
# # # obj = MinStack()
# # # obj.push(val)
# # # obj.pop()
# # # param_3 = obj.top()
# # # param_4 = obj.getMin()
# class MinStack:

#     def __init__(self):
#         self.st = []

#     def push(self, val: int) -> None:
#         min_val = self.getMin()
#         if min_val == None or min_val > val:
#             min_val = val
        
#         self.st.append([val, min_val])

#     def pop(self) -> None:
#         self.st.pop()

#     def top(self) -> int:
#         return self.st[-1][0] if self.st else None

#     def getMin(self) -> int:
#         return self.st[-1][1] if self.st else None