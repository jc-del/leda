#include <cstdio>
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, xi, yi, xf,yf;

    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        cin>>xi>>yi>>xf>>yf;
      /*  scanf("%d", &xi);
        scanf("%d", &yi);
        scanf("%d", &xf);
        scanf("%d", &yf);*/
    }
    printf("%d\n", xi);
    printf("%d\n", xf);
    printf("%d\n", yi);
    printf("%d\n", yf);
    int rx = (xi+1);
    int ry = (yi +1);
    bool foundx = false;
    bool foundy = false;
    int ans = 0;
    while(!foundx){
        if(rx-1 == xf) foundx = true;
        else if (rx != xi){
            if (xi>rx){
                ans+=1;
                //xi+=1;
                rx+=1;
            }
            else if (xi<rx)
                ans+=1;
                //xi-=1;
                rx-=1;
        }
    }
    while(!foundy){
        if(ry-1 == yf) foundy = true;
        else if (ry != yi){
            if (yi>ry){
                ans+=1;
                //yi+=1;
                ry+=1;
            }
            else if (xi<rx)
                ans+=1;
                //yi-=1;
                ry-=1;
        }
    }

    printf("%d\n", ans);
    return 0;
}

