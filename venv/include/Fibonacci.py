# F0 = 0 , F1=1
# # Fn = F(n-1) + F(n-2) (n>=2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input())))