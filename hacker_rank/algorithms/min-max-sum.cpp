#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int a[] = {1,2,3};
	cout << sizeof(a)/sizeof(a[0]);
	return 0;
}