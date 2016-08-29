// https://www.hackerrank.com/challenges/vector-sort

#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){	
	int size;
	cin >> size;
	vector<int> items;
	int item;
	for (int i = 0; i < size; ++i)
	{
		cin >> item;
		items.push_back(item);	
	}

	sort(items.begin(), items.end());

	for (int i = 0; i < size; ++i)
	{
		cout << items[i]<< " ";
	}

}