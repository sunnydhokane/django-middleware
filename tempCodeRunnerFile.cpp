#include<bits/stdc++.h>
using namespace std;
int main(){
    cout<<"Enter number of Node and Edges in a Graph :";
    int n,m;
    cin>>n>>m;
    cout<<"Enter The heuristic distance of each node from the target Node :";
    vector<int> v(n);
    for(int i=0;i<n;i++) cin>>v[i];
    cout<<"Enter The edges that exists between the nodes\n";
    vector<int> graph[n];
    for(int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    cout<<"Enter the Start Node :";
    int st;
    cin>>st;
    cout<<"Enter Target Node :";
    int target;
    cin>>target;
    vector<int> ans;
    int flag=0;
    multiset<pair<int,pair<int,int>>> q;
    vector<int> vis(n,0);
    st=0;
    q.insert({v[st],{0,st}});
    vis[st]=1;
    int cnt=1;
    while(q.size()>0){
        auto k=*q.begin();
        q.erase(q.begin());
       
        if(k.second.second==target){
            flag=1;
            ans.push_back(target);
            break;
        }
        ans.push_back(k.second.second);
        for(auto &x:graph[k.second.second]){
            if(vis[x]==0){
                vis[x]=1;
                q.insert({v[x],{cnt,x}});
                cnt++;
            }
            
        }
    }
    if(flag){
        cout<<"Path Found \n";
        cout<<"Nodes visited are :";
        for(auto &x:ans) cout<<x<<" ";
        cout<<endl;
        
    }
    else{
        cout<<"Path Not Found\n";
    }

    

}