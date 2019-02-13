#include <iostream>
#include "Stack.h"
#include <cstdlib>

using namespace std;

int main(){
  Stack<int,10> mystack;
  mystack.push(rand()%100);
  mystack.push(rand()%100);
  mystack.push(rand()%100);
  try{
    while(1) {
      cout << mystack.pop() << " ";
    }
  }
  catch(const char * message)
  {
    cout << message << endl;
  }
  return 0;
}
