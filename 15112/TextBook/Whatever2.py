def f(s,t,n):
    q=''
    for i in range (len(s)):
        q+=t[(i+n)%len(t)]
    return ((len(s) == 2 * len(t)) and (not s.startswith(t)) and q==s)

print(f('baba','ab',1))