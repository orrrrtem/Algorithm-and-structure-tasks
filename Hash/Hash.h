//
// Created by Артем Аросланкин on 02/12/2018.
//

#ifndef HASH_HASH_H
#define HASH_HASH_H

#include <iostream>
#include <cstring>
#include <cstring>
using namespace std;

class LinkedHashEntry {
private:
    int key;
    string value;
    LinkedHashEntry *next;
public:
    LinkedHashEntry(int key, string value) {
        this->key = key;
        this->value = value;
        this->next = NULL;
    }

    int getKey() {
        return key;
    }

    string getValue() {
        return value;
    }

    void setValue(int value) {
        this->value = value;
    }

    LinkedHashEntry *getNext() {
        return next;
    }

    void setNext(LinkedHashEntry *next) {
        this->next = next;
    }
};


class HashEntry {
private:
    int key;
    int value;
public:
    HashEntry(int key, int value) {
        this->key = key;
        this->value = value;
    }

    int getKey() {
        return key;
    }

    int getValue() {
        return value;
    }

    void setValue(int value) {
        this->value = value;
    }
};

#endif //HASH_HASH_H
