#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[]){
	int n,m;
	cin >> n >> m;
	long int a,b;
	long int c[m];
	int pre_mat[n][m];
	for (int i = 0; i < m; ++i){
		for (int j = 0; j < n; ++j){
			pre_mat[i][j] = 0;
		}
	}

	long int seq[n];
	long int max = 0;
	for (int i = 0; i < m; ++i){
		cin >> a >> b >> c[i];
		for (int j = a-1; j < b; ++j){
				pre_mat[i][j] = 1;
		}
		for (int j = 0; j < n; ++j){
			cout << pre_mat[i][j] << "\t";
		}
		cout << "\n";
	}

	// for(int i=0; i<n; i++){
	// 	long int value = 0;
	// 	for(int j=0; j<m;j++){
	// 		value += (pre_mat[j][i]*c[j]);
	// 	}
	// 	if(value > max){
	// 		max = value;
	// 	}
	// }

	// for (int i = 0; i < m; ++i){
	// 	for (int j = 0; j < n; ++j){
	// 		cout << pre_mat[i][j] << "\t";
	// 	}
	// 	cout << "\n";
	// }

	cout << max;
	return 0;
}
