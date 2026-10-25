#!/usr/bin/env python3

RED_RANKS={0,2,5,6}

def colour(s):
    return (s.bit_count() in RED_RANKS)

def graph_vertices(red):
    return [s for s in range(256) if colour(s)==red]

def adjacency(vertices, red):
    adj=[set() for _ in vertices]
    for i,a in enumerate(vertices):
        for j in range(i+1,len(vertices)):
            b=vertices[j]
            if colour(a|b)==red and colour(a&b)==red:
                adj[i].add(j); adj[j].add(i)
    return adj

def maximum_clique(adj):
    best=[]
    def expand(clique, candidates):
        nonlocal best
        if len(clique)+len(candidates)<=len(best):
            return
        while candidates:
            if len(clique)+len(candidates)<=len(best):
                return
            candset=set(candidates)
            v=max(candidates,key=lambda x: len(adj[x] & candset))
            newc=[u for u in candidates if u in adj[v]]
            expand(clique+[v], newc)
            candidates=[u for u in candidates if u!=v]
        if len(clique)>len(best):
            best=clique
    expand([], list(range(len(adj))))
    return best

for red,name,expected_v,expected_e,expected_w in [
    (True,'red',113,1260,4), (False,'blue',143,2326,5)]:
    V=graph_vertices(red); A=adjacency(V,red)
    edges=sum(map(len,A))//2
    C=maximum_clique(A)
    print(name, 'vertices=',len(V),'edges=',edges,'omega=',len(C),
          'witness=',[(V[i],V[i].bit_count()) for i in C])
    assert len(V)==expected_v and edges==expected_e and len(C)==expected_w
print('INDEPENDENT PYTHON CHECK PASSED; f(8)=5 follows with the maximal-chain lower bound.')
