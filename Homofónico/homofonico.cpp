#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>

using namespace std;

int TABLE_SIZE = 100;

template <typename T>
void printVector(const vector<T>& vector1) {
    for (long unsigned int i = 0; i < vector1.size(); i++) {
        cout << vector1[i] << " ";
    }
    cout << endl;
}
template <typename T>
void printVector(const vector<vector<T>>& vector1) {
    for (long unsigned int i = 0; i < vector1.size(); i++) {
        for (long unsigned int j = 0; j < vector1[i].size(); j++) {
            cout << vector1[i][j] << " ";
        }
        cout << endl;
    }
}

string fixText(string text){
    for (int i = 0; i < text.length(); i++){
        text.at(i) = tolower(text.at(i));
    }
    text.erase(
        remove_if(text.begin(), text.end(), [](char x) {
            return (x > 'z' || x < 'a');
        }), text.end()
    );
    return text;
}

vector<char> arrangeKey(const vector<vector<short>>& encTable) {
    vector<char> decTable(TABLE_SIZE);
    char c;
    for (int i = 0; i < encTable.size(); i++) {
        c = (char)i+'a';
        // cout << encTable[i].size() << " ";
        for (long unsigned int j = 0; j < encTable[i].size(); j++) {
            decTable[encTable[i][j]] = c;
        }
    }
    return decTable;
}

vector<short> encrypt(string cleartext, const vector<vector<short>>& encTable, mt19937& gen) {
    cleartext = fixText(cleartext);
    int sizeMessage = cleartext.size();
    short letter;
    vector<short> ciphertext(sizeMessage);
    uniform_int_distribution<> dis;

    for (int i = 0; i < sizeMessage; i++) {
        letter = cleartext.at(i) - 'a';
        dis.param(uniform_int_distribution<>::param_type(0, encTable[letter].size() - 1)); // distribucion uniforme en el rango de numeros posibles
        ciphertext[i] = encTable[letter][dis(gen)];
    }
    return ciphertext;
}

string decrypt(const vector<short>& ciphertext, const vector<vector<short>>& encTable) {
    string cleartext = "";
    int sizeMessage = ciphertext.size();
    vector<char> decTable = arrangeKey(encTable);
    for (int i = 0; i < sizeMessage; i++) {
        cleartext += decTable[ciphertext[i]];
    }
    return cleartext;
}

int main()
{
    // vector con la tabla para encriptar
    std::vector<vector<short>> encTable(26);
    encTable[0] = {9, 12, 33, 47, 53, 67, 78, 92};
    encTable[1] = {48, 81};
    encTable[2] = {13, 41, 62};
    encTable[3] = {1, 3, 45, 79};
    encTable[4] = {14, 16, 24, 44, 46, 55, 57, 64, 74, 82, 87, 98};
    encTable[5] = {10, 31};
    encTable[6] = {6, 25};
    encTable[7] = {23, 39, 50, 56, 65, 68};
    encTable[8] = {32, 70, 73, 83, 88, 93};
    encTable[9] = {15};
    encTable[10] = {4};
    encTable[11] = {26, 37, 51, 84};
    encTable[12] = {22, 27};
    encTable[13] = {18, 58, 59, 66, 71, 91};
    encTable[14] = {0, 5, 7, 54, 72, 90, 99};
    encTable[15] = {38, 95};
    encTable[16] = {94};
    encTable[17] = {29, 35, 40, 42, 77, 80};
    encTable[18] = {11, 19, 36, 76, 86, 96};
    encTable[19] = {17, 20, 30, 43, 49, 69, 75, 85, 97};
    encTable[20] = {8, 61, 63};
    encTable[21] = {34};
    encTable[22] = {60, 89};
    encTable[23] = {28};
    encTable[24] = {21, 52};
    encTable[25] = {2};

    // 1. Seed (true random source)
    random_device rd;

    // 2. Engine (pseudo-random generator)
    mt19937 gen(rd());  // Mersenne Twister (excellent quality)

    //printVector(encTable);
    string cleartext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG";

    cout << "Text: " << cleartext << endl;
    vector<short> ciphertext = encrypt(cleartext, encTable, gen);
    cout << "Ciphertext: ";
    printVector(ciphertext);

    cleartext = decrypt(ciphertext, encTable);
    cout << "Cleartext: " << cleartext << endl;

    vector<short> test1 = {62, 40, 21, 95, 69, 90, 32, 19, 31, 61, 91};
    cleartext = decrypt(test1, encTable);
    cout << "Test1: " << cleartext << endl;

    vector<short> test2 = {13 ,5 ,26 ,0 ,22 ,81 ,88 , 47};
    cleartext = decrypt(test2, encTable);
    cout << "Test2: " << cleartext << endl;
    return 0;
}
