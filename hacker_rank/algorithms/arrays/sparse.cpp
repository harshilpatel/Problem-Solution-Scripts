#include <iostream>
#include <map>

using namespace std;

int main(int argc, char const *argv[])
{	
	int n;
	string temp;
	cin >> n;
	map<string, int> seq;

	for(int i=0;i<n;i++){
		cin >> temp;
		seq[temp] += 1;
	}

	int d;
	cin >> d;
	for (int i = 0; i < d; ++i){
		cin >> temp;
		cout << seq[temp] << "\n";
	}


	return 0;
}