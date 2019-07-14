#include <iostream>
#include "Hash.h"
#include "hashFun.h"
#include <ctime>
#include <time.h>
#include <string>
#include <vector>

using namespace std;

#define PRIME 7717;


int main() {
    string str = "Artem";
    int ans = 0;
    for( int i = 0; i < str.length(); i++) {
        ans += ((int) str[i]) * i^3;
        ans = ans % PRIME;
    }
    cout << ans;
    int n = 5;
    LinkedHashEntry s(ans, str);
    *
    return 0;
}