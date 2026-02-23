#Finger exercise lecture 4

n = 8
# =============================================================================
# cuberoot = n**(1/3)
# 
# if cuberoot.is_integer():
#     print(cuberoot)
# else:
#     print("error")
# =============================================================================

count = 0
while count**3 < n:
    count += 1
if count**3 == n:
    print(count)
else:
    print("error")