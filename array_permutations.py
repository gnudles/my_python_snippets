def rotate_right(a,from_):
    b=[]
    b.extend(a[0:from_])
    b.append(a[-1])
    b.extend(a[from_:-1])
    return b

def rotate_left(a,from_):
    b=[]
    b.extend(a[0:from_])
    b.extend(a[from_+1:])
    b.append(a[from_])
    return b

def permutate(a,from_):
     if (from_+1>=len(a)):
         print(a)
         return
     for i in range(len(a)-from_):
         permutate(a,from_+1)
         a=rotate_left(a,from_)


def permutate_loop(a):
     n=len(a)
     l=0;
     c=[0]
     while (True):
         if(c[-1]<n-l):
             c[-1]+=1
             if(l+2>=n):
                 print (a)
                 a=rotate_left(a,l)
             else:
                 c.append(0)
                 l+=1;
         else:
             c.pop()
             if(l==0):
                 return;
             l-=1
             a=rotate_left(a,l)

#usage:

a=[0,1,2,3]
permutate_loop(a)

