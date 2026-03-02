#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string fixText(string text){
    text.erase(
        remove_if(text.begin(), text.end(), [](char x) {
            return (x > 'z' || x < 'a');
        }), text.end()
    );
    return text;
}

string encrypt(string cleartext, string key){
    cleartext = fixText(cleartext);
    string ciphertext = "";
    return ciphertext;
}

string decrypt(string ciphertext, string key) {
    key = fixText(key);
    string cleartext = "";
    return cleartext;
}

int main()
{
    string cleartext = "Crypto is fun";
    string key = "relations ";

    string ciphertext = encrypt(cleartext, key);
    cout << "Ciphertext: " << ciphertext << endl;
    cleartext = decrypt(ciphertext, key);
    cout << "Cleartext: " << cleartext << endl;

    return 0;
}
