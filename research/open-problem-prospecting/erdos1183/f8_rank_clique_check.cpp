#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using U64 = uint64_t;

struct MaxClique {
    int n;
    int words;
    std::vector<std::vector<U64>> adj;
    int best = 0;
    std::vector<int> best_clique;

    explicit MaxClique(int n_) : n(n_), words((n+63)/64), adj(n, std::vector<U64>(words)) {}

    void add_edge(int a, int b) {
        adj[a][b>>6] |= U64(1) << (b&63);
        adj[b][a>>6] |= U64(1) << (a&63);
    }

    static int popcount(const std::vector<U64>& b) {
        int s=0; for (U64 x: b) s += std::popcount(x); return s;
    }
    static bool empty(const std::vector<U64>& b) {
        for (U64 x: b) if (x) return false; return true;
    }
    static void clearbit(std::vector<U64>& b, int v) { b[v>>6] &= ~(U64(1)<<(v&63)); }
    static bool testbit(const std::vector<U64>& b, int v) { return (b[v>>6]>>(v&63))&1; }
    static int firstbit(const std::vector<U64>& b) {
        for (int w=0; w<(int)b.size(); ++w) if (b[w]) return (w<<6) + std::countr_zero(b[w]);
        return -1;
    }
    std::vector<U64> intersect(const std::vector<U64>& a, const std::vector<U64>& b) const {
        std::vector<U64> c(words); for(int i=0;i<words;++i)c[i]=a[i]&b[i]; return c;
    }
    std::vector<U64> difference(const std::vector<U64>& a, const std::vector<U64>& b) const {
        std::vector<U64> c(words); for(int i=0;i<words;++i)c[i]=a[i]&~b[i];
        if (n%64) c.back() &= (U64(1)<<(n%64))-1;
        return c;
    }

    void bronk(std::vector<int>& R, std::vector<U64> P, std::vector<U64> X) {
        if ((int)R.size() + popcount(P) <= best) return;
        if (empty(P) && empty(X)) {
            if ((int)R.size() > best) { best = R.size(); best_clique = R; }
            return;
        }
        int pivot=-1, score=-1;
        for(int v=0;v<n;++v) if(testbit(P,v)||testbit(X,v)) {
            int s=0; for(int w=0;w<words;++w) s += std::popcount(P[w]&adj[v][w]);
            if(s>score){score=s;pivot=v;}
        }
        std::vector<U64> ext = (pivot>=0) ? difference(P, adj[pivot]) : P;
        while(!empty(ext)) {
            int v=firstbit(ext);
            clearbit(ext,v);
            R.push_back(v);
            bronk(R, intersect(P, adj[v]), intersect(X, adj[v]));
            R.pop_back();
            clearbit(P,v);
            X[v>>6] |= U64(1)<<(v&63);
            if ((int)R.size() + popcount(P) <= best) return;
        }
    }

    int solve() {
        std::vector<U64> P(words, ~U64(0)), X(words,0);
        if(n%64) P.back() &= (U64(1)<<(n%64))-1;
        std::vector<int> R;
        bronk(R,P,X);
        return best;
    }
};

static int rank8(int x) { return std::popcount((unsigned)x); }

int main(){
    const std::array<bool,9> redRank = {true,false,true,false,false,true,true,false,false};
    for(int color=0;color<2;++color){
        std::vector<int> verts;
        for(int s=0;s<256;++s){
            bool red=redRank[rank8(s)];
            if(red==(color==0)) verts.push_back(s);
        }
        MaxClique mc((int)verts.size());
        long long edges=0;
        for(int i=0;i<(int)verts.size();++i) for(int j=i+1;j<(int)verts.size();++j){
            int a=verts[i],b=verts[j];
            int u=a|b, in=a&b;
            bool cu=redRank[rank8(u)]==(color==0);
            bool ci=redRank[rank8(in)]==(color==0);
            if(cu&&ci){mc.add_edge(i,j);++edges;}
        }
        int omega=mc.solve();
        std::cout << (color==0?"red":"blue") << " vertices="<<verts.size()<<" edges="<<edges<<" omega="<<omega<<" witness=";
        for(int idx:mc.best_clique){
            int s=verts[idx]; std::cout<<s<<"(r"<<rank8(s)<<") ";
        }
        std::cout<<"\n";
        if(color==0 && omega!=4) return 2;
        if(color==1 && omega!=5) return 3;
    }
    std::cout << "Therefore every monochromatic union/intersection-closed family has size <=5.\n";
    std::cout << "The 9-set maximal chain forces a monochromatic 5-set subchain, so f(8)=5.\n";
    return 0;
}
