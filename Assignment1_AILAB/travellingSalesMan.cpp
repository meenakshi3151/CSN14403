#include <bits/stdc++.h>
using namespace std;
int tsp(vector<vector<int>> &graph, int s) {
    int V = graph.size();

    vector<int> vertex;
    for (int i = 0; i < V; i++)
        if (i != s)
            vertex.push_back(i);

    int min_cost = INT_MAX;
    while (next_permutation(vertex.begin(), vertex.end())) {
        int current_cost = 0;
        int j = s;
        for (int i = 0; i < vertex.size(); i++) {
            current_cost += graph[j][vertex[i]];
            j = vertex[i];
        }
        current_cost += graph[j][s];
        min_cost = min(min_cost, current_cost);
    }
    return min_cost;
}

int main() {
    cout << "Enter number of vertices:";
    int V;
    cin >> V;

    vector<vector<int>> graph(V, vector<int>(V, 0));

    cout << "Enter the adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cin >> graph[i][j];
        }
    }
    cout << "Enter the source vertex:";
    int s;
    cin >> s;
    cout << tsp(graph, s) << endl;
    return 0;
}
