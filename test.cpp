#include <vector>
#include <algorithm>
#include <iostream>

void test(std::vector<int>& queue, int detection) {
    queue.push_back(detection);
    std::sort(queue.begin(), queue.end(), [](const int& a, const int& b) {
        return a > b;
    });
}

int main(){
    std::vector<int> a;
    for(int i=0; i<=10; i++){
        test(a, i);
    }
    test(a, 3);
    for (auto e : a) {
        std::cout << e << " ";
    }
}