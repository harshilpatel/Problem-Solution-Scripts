#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	int size;
	int a,b;
	cin >> size;
	std::vector<int> v;
	for (int i = 0; i < size; ++i)
	{
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	cin >> a;
	if(a < v.size()) v.erase(v.begin() + a - 1);

	cin >> a >> b;
	if(a < b && b-1<=v.size()) v.erase(v.begin() + a -1, v.begin() + b-1);	

	cout << v.size() << endl;

	for (int i = 0; i < v.size(); ++i)
	{
		cout << v[i] << " ";
	}


	return 0;
}
