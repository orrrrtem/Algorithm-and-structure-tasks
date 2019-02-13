//
// Created by Артем Аросланкин on 12/02/2019.
//

#ifndef DEANARY_DEANERY_H
#define DEANARY_DEANERY_H

#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>

using namespace std;
class Group;

class Student{
private:
    unsigned int id;
    string fio;
    Group* group;
    vector<unsigned int> marks;
    size_t num = marks.size();
    double avg;
public:
    Student(unsigned int id, string fam);
    Student(unsigned int id, string fam, Group* group);
    void attend(Group* group);
    Group* getgroup() const;
    void addmark(unsigned int mark);
    vector<unsigned int> getmarks() const;
    size_t getnum() const;
    double calcavg() const;
    double getavg() const;
    string getfio() const;
    void setd(unsigned int id);
    unsigned int getd() const;
};



class Group{
private:
    string title;
    vector<Student*> list;
    size_t num = list.size();
    Student* head;
    vector<int> search_(string fio) const;
    int search_(unsigned int id) const;
public:
    Group(string title);
    void add(Student* st);
    void voting();
    void print() const;
    vector<Student*> search(string fio) const;
    Student* search(unsigned int id) const;

    double getavg() const;
    double getavg2() const;
    void exclude(Student* st);

};


class Deanery{
private:
    vector<Student*> students;
    vector<Group*> groups;
public:
    Deanery();
    Deanery(string input);



};
#endif //DEANARY_DEANERY_H
