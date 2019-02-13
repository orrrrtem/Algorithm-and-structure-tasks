#include <iostream>
#include "deanery.h"

int main() {

    Student s1(1,"Aroslankin A.D.");
    Student s4(12,"Aroslankin A.D.");
    Student s2(5,"Kuklin M.I.");
    s1.addmark(5);
    s1.addmark(3);
    s4.addmark(5);
    Group g1("PMI");
    s1.attend(&g1);
    s2.attend(&g1);
    s4.attend(&g1);
    g1.voting();
    g1.print();
    g1.exclude(&s4);
    cout << endl;
    g1.print();

    int id;
    string fam, input= "/Users/artemaroslankin/Documents/Progacpp/deanary/groups.txt";

    ifstream file(input);
    if (file.is_open()) {

        string id = "";
        string fio = "";
        string buf = "";
        int len;
        while (getline(file, buf)) {
            len = buf.size();
            if (buf[0] == 'h'){
                Student
            }


        }
    }


    return 0;
}