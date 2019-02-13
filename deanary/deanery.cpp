//
// Created by Артем Аросланкин on 12/02/2019.
//
#include "deanery.h"

Student::Student(unsigned int id, string fam){
    this->id = id;
    this->fio = fam;
    this->group = NULL;
}

Student::Student(unsigned int id, string fam, Group* group){
    this->id = id;
    this->fio = fam;
    this->group = group;
}

void Student::attend(Group* group){
    this->group = group;
    group->add(this);
}

void Student::addmark(unsigned int mark){
    marks.push_back(mark);
    num ++;
    this->avg = calcavg();
}

vector<unsigned int> Student::getmarks() const{
    vector<unsigned int> ans;
    ans = this->marks;
    return ans;
}
size_t Student::getnum() const{
    return this->num;
}

double Student::calcavg() const{
    double ans = 0;
    for(int i = 0; i < num;i++)
        ans = ans + marks[i];
    ans = ans / num;
    return ans;
}
Group* Student::getgroup() const {
    return this->group;
}
double Student::getavg() const {
    return this->avg;
}

void Student::setd(unsigned int id) {
    this->id = id;
}

unsigned int Student::getd() const {
    return this->id;
}
string Student::getfio() const {
    return this->fio;
}







Group::Group(string title) {
    this->title = title;
}

void Group::add(Student *st) {
    for(int i=1; i < num; i++){
        if(st->getd() == list[i]->getd())
            if(st->getfio() == list[i]->getfio()) {
                cout << "Probabilty of Student" << st->getfio() << "beeing already in group";
                cout << "Change id, if it is wrong";
                cout << endl;
                return;
            }
            else{
                unsigned int k = 1;

                while(k<1000000){
                    int p = 0;
                    for(int i=1; i < num; i++)
                        if(list[i]->getd()!=k)
                            p++;
                    if(p == this->num){
                        st->setd(k);
                        list.push_back(st);
                        num++;
                        return;
                    }
                    k++;

                }
                cout << "Error:The group is full!";
                cout << endl;
                return;
            }
    }
    list.push_back(st);
    num++;
}

void Group::voting(){
    double avgmax = 0;
    head = list[0];
    for(int i=1; i < num; i++)
        if(avgmax <= list[i]->getavg())
            head = list[i];
}

void Group::print() const {
    for(int i=0; i < num; i++){
        if(list[i]==head) cout <<"Head ";
        cout <<"id: "<<list[i]->getd() << "   ; FIO: " << list[i]->getfio();
        cout << endl;
    }
}

vector<Student*> Group::search(string fio) const {
    vector<Student*> res;
    for(int i=0; i < num; i++){
       if(list[i]->getfio() == fio)
           res.push_back(list[i]);
    }
    return res;

}

Student* Group::search(unsigned int id) const {
    for(int i=0; i < num; i++){
        if(list[i]->getd() == id)
            return list[i];
    }
    return NULL;
}

vector<int> Group::search_(string fio) const {
    vector<int> res;
    for(int i=0; i < num; i++){
        if(list[i]->getfio() == fio)
            res.push_back(i);
    }
    return res;

}

int Group::search_(unsigned int id) const {
    for(int i=0; i < num; i++){
        if(list[i]->getd() == id)
            return i;
    }
    return -1;
}


double Group::getavg() const {
    double sum = 0;
    int k = 0;
    for(int i=0; i < num; i++) {
        if((list[i]->getmarks()).size() == 0)
            k++;
        else
            sum = sum + list[i]->getavg();
    }
    sum = sum / (num-k);
    return sum;
}

double Group::getavg2() const {
    double sum = 0;
    int n = 0;
    for(int i=0; i < num; i++) {
        for (int j = 0; j < list[i]->getnum(); j++)
            sum = sum + (list[i]->getmarks())[j];
        n = n + (list[i]->getmarks()).size();
    }
    sum = sum / n;
    return sum;
}

void Group::exclude(Student* st) {
    int k = this->search_(st->getd());
    if(head != list[k]) {
        list.erase(list.begin() + k);
        num = num - 1;
    }
    else
        list.erase(list.begin() + k);
        num = num - 1;
        voting();
}




Deanery::Deanery(string input) {
    ifstream file(input);
    if (!file) {
        cout << "File " << input << " opening Error ";
        return;
    } else {
        string id = "";
        string fio = "";
        char buf[80];
        file.getline(buf, 80);
        int len = strlen(buf);
    }
}
