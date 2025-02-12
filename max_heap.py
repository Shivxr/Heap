def parent(ind):
    if (ind-1)//2>=0:
        return (ind-1)//2
    return -1

def left(ind,ln):
    if (ind*2)+1<ln:
        return (ind*2)+1
    return -1

def right(ind,ln):
    if (ind*2)+2<ln:
        return (ind*2)+2
    return -1

def lar(ind,hp,ln):
    lar=-1
    l,r=left(ind,ln),right(ind,ln)
    if l!=-1 and r!=1:
        if hp[l]>hp[r]:
            lar=l
        else:
            lar=r
    elif (l*r)<0:
        if l!=-1:
            lar=l
        else:
            lar=r
    return lar
        
    

def heapify(arr):
    hp=[]
    for i in range(len(arr)):
        hp.append(arr[i])
        while parent(i)!=-1 and hp[parent(i)]<hp[i]:
            hp[i],hp[parent(i)]=hp[parent(i)],hp[i]
            i=parent(i)
    return hp

def hins(a,hp):
    hp.append(a)
    i=len(hp)-1
    while parent(i)!=-1 and hp[parent(i)]<hp[i]:
            hp[i],hp[parent(i)]=hp[parent(i)],hp[i]
            i=parent(i)
            
def hdel(ind,hp):
    hp[ind],hp[-1]=hp[-1],hp[ind]
    hp.pop()
    x=lar(ind,hp,len(hp))
    while x!=-1 and hp[ind]<hp[x]:
        z=lar(ind,hp,len(hp))
        hp[ind],hp[x]=hp[x],hp[ind]
        ind=z
        x=lar(ind,hp,len(hp))
