// https://www.hackerrank.com/challenges/cpp-lower-bound

#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int size;
	cin >> size;
	vector<int> v;
	int temp;
	
	//  taking in values
	for (int i = 0; i < size; ++i)
	{
		cin >> temp;
		v.push_back(temp);
	}

	int cases;
	cin >> cases;
	int val;
	for (int i = 0; i < cases; ++i)
	{
		cin >> val;
		vector<int>::iterator up = lower_bound(v.begin(), v.end(), val);
		if ( v[up - v.begin()] == val ) cout << "Yes " << up - v.begin() +1 << "\n";
		else cout << "No " << up - v.begin() +1 << "\n";

	}
	return 0;
}