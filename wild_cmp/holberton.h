#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <stdlib.h>

int _strlen_recursion(char *s);
int wildcmp(char *s1, char *s2);
int _wildcmp_recursion(int i, int j, char *s1, char *s2);
int search_char(int i, int j, char*s1, char *s2);

#endif
