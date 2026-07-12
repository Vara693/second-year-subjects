#include <iostream>
#include <vector>
using namespace std;

#define INF 9999

int main() {
    int n;
    cout << "Enter number of routers: ";
    cin >> n;

    vector<vector<int>> cost(n, vector<int>(n));
    vector<vector<int>> dist(n, vector<int>(n));

    cout << "Enter cost matrix:\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> cost[i][j];
            dist[i][j] = cost[i][j];
        }
    }

    // Bellman-Ford style iterations (Distance Vector)
    for(int iter = 0; iter < n - 1; iter++) {
        for(int i = 0; i < n; i++) {        // source router
            for(int j = 0; j < n; j++) {    // destination
                for(int k = 0; k < n; k++) { // neighbor
                    if(cost[i][k] != INF && dist[k][j] != INF) {
                        if(dist[i][j] > cost[i][k] + dist[k][j]) {
                            dist[i][j] = cost[i][k] + dist[k][j];
                        }
                    }
                }
            }
        }
    }

    cout << "\nDistance Vector Table:\n";
    for(int i = 0; i < n; i++) {
        cout << "Router " << i << ": ";
        for(int j = 0; j < n; j++) {
            if(dist[i][j] == INF)
                cout << "INF ";
            else
                cout << dist[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\nCost Vector Table:\n";
    for(int i = 0; i < n; i++) {
        cout << "Router " << i << ": ";
        for(int j = 0; j < n; j++) {
            if(dist[i][j] == INF)
                cout << "INF ";
            else
                cout << dist[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}