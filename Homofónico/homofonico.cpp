#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

template <typename T>
void printVector(vector<T> vector1) {
    for (long unsigned int i = 0; i < vector1.size(); i++) {
        cout << vector1[i] << " ";
    }
    cout << endl;
}

string fixText(string text){
    //text.tolower()
    text.erase(
        remove_if(text.begin(), text.end(), [](char x) {
            return (x > 'z' || x < 'a');
        }), text.end()
    );
    return text;
}

vector<char> encriptionKey(vector<short> encTable[26]) {
    vector<char> decTable(100);
    char c;
    for (int i = 0; i < 26; i++) {
        c = (char)i+'a';
        // cout << encTable[i].size() << " ";
        for (int j = 0; j < encTable[i].size(); j++) {
            decTable[encTable[i][j]] = c;
        }
        // cout << c << endl;
    }
    // printVector(decTable);
    return decTable;
}

vector<short> encrypt(string cleartext, vector<short> encTable[26]) {
    cleartext = fixText(cleartext);
    // cout << cleartext << endl;
    int sizeMessage = cleartext.size();
    int randomNumber, possibleEncryptions;
    short letter;
    vector<short> ciphertext(sizeMessage);

    srand(time(nullptr));
    for (unsigned int i = 0; i < sizeMessage; i++) {
        letter = cleartext.at(i) - 'a';
        randomNumber = rand();
        possibleEncryptions = encTable[letter].size();
        while (randomNumber < 0) {
            randomNumber = randomNumber + possibleEncryptions;
        }
        randomNumber = randomNumber % possibleEncryptions;
        ciphertext[i] = encTable[letter][randomNumber];
    }
    return ciphertext;
}

string decrypt(vector<short> ciphertext, vector<short> encTable[26]) {
    string cleartext = "";
    sizeMessage = ciphertext.size();
    decTable = encriptionKey(encTable);
    for (int i = 0; i < sizeMessage; i++) {
        cleartext += decTable[i];
    }
    return cleartext;
}

int main()
{
    // vector con la tabla para encriptar
    std::vector<short> encTable[26];
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

    string cleartext = "crypto is fun";

    cout << "Text: " << cleartext << endl;
    vector<short> ciphertext = encrypt(cleartext, encTable);
    cout << "Ciphertext: ";
    printVector(ciphertext);

    cleartext = decrypt(ciphertext, encTable);
    cout << "Cleartext: " << cleartext << endl;
    return 0;
}
