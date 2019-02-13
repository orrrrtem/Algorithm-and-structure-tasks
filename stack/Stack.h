template <typename T, int size = 100>

class Stack
{
private:
  T data[size];
  T top;
public:
  Stack():top(-1) {}

  void push(T elem){
    if(top < size)
      data[++top] = elem;
    else
        throw "Stack is full";
  }
  T get() const {
    if(top >= 0)
      return data[top];
    else
      throw "Stack is empty";
  }

  void pop() {
    if(top >= 0)
      return data[--];
    else
      throw "Stack is empty";
  }

  bool isEmpty() const {
    return top == -1;
  }

  bool isFull() const {
    return top == size - 1;
  }
};
