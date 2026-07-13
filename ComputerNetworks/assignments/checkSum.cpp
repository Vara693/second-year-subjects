#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;
//finction 1: Addition
string addBin(string &a, string &b) {
    string result = "";
    int i=a.size()-1;
    int j= b.size()-1;
    int carry = 0;
    while (i>=0 || j>=0 || carry) {
        int sum = carry;
        if (i>=0) sum+=a[i--]-'0';
        if (j>=0) sum+=b[j--]-'0';
        result.push_back(sum%2+'0');
        carry = sum/2;
    }
    reverse(result.begin(), result.end());
    return result;
}

//function 2: The loop on the vector
string loopString(vector<string> &binaries) {
    string result = binaries[0];
    for (int i=1; i<binaries.size(); i++) {
        result = addBin(result, binaries[i]);
        while (result.size()>binaries[i].size()) {
            string carry = result.substr(0, result.size() - binaries[i].size());
            string part  = result.substr(result.size() - binaries[i].size());
            result = addBin(carry, part);
        }
    }
    return result;
}

//function 3: checkSum
string checkSum(vector<string> &binaries) {
    string result = loopString(binaries);
    string complement = "";
    for (char &c: result) {
        char ch = (c=='0')? '1': '0';
        complement.push_back(ch);
    }

    return complement;
}
int main() {
    auto start = high_resolution_clock::now();

    vector<string> binaries = {"1010", "1100", "0110"};
    string addition = loopString(binaries);
    string check = checkSum(binaries);

    cout << "Addition of all binaries: " << addition << endl;
    cout << "Check sum: " << check << endl;
    cout << "The result: " << addBin(addition, check) << endl;

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Execution time: " << duration.count() << " microseconds" << endl;
    return 0;
}