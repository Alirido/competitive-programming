/*	
	A. Two Regular Polygons
	Time limit 1 s
	Memory Limit 256 MB
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	while (t--) {
		int n, m;
		scanf("%d %d", &n, &m);
		printf("%s\n", n%m == 0 ? "YES" : "NO");
	}

	return 0;
}