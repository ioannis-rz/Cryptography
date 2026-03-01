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
    key = fixText(key);
    int textSize = cleartext.length();
    int keySize = key.length();
    if (keySize <= 0){
        throw std::runtime_error("Llave no válida");
    }

    string ciphertext = "";
    for (int i = 0; i < textSize; i++){
        int temp = (key.at(i % keySize) + cleartext[i] - ('a'*2)) % 26;
        ciphertext += (temp+'a');
    }
    return ciphertext;
}

string encrypt(string cleartext, string key, int t){
    cleartext = fixText(cleartext);
    key = fixText(key);
    int textSize = cleartext.length();
    int keySize = key.length();
    if (keySize <= 0){
        throw std::runtime_error("Llave no válida");
    }

    string ciphertext = "";
    for (int i = 0, j = 0; i < textSize; i++){
        if (j == t) {
            rotate(key.begin(), key.begin() + 1, key.end());
            j = 0;
        }

        int temp = (key.at(i % keySize) + cleartext[i] - ('a'*2)) % 26;
        ciphertext += (temp+'a');
        j++;
    }
    return ciphertext;
}

string decrypt(string ciphertext, string key) {
    key = fixText(key);
    int textSize = ciphertext.length();
    int keySize = key.length();
    if (keySize <= 0){
        throw std::runtime_error("Llave no válida");
    }

    string cleartext = "";

    for (int i = 0; i < textSize; i++){
        int temp = (ciphertext[i] - key.at(i % keySize));
        temp += 26; // por si acaso es negativo el resultado, en cuyo caso solo hace falta sumar una vez
        temp = temp % 26;
        cleartext += (temp+'a');
    }

    return cleartext;
}

string decrypt(string ciphertext, string key, int t) {
    key = fixText(key);
    int textSize = ciphertext.length();
    int keySize = key.length();
    if (keySize <= 0){
        throw std::runtime_error("Llave no válida");
    }

    string cleartext = "";

    for (int i = 0 ,j = 0; i < textSize; i++){
        if (j == t) {
            rotate(key.begin(), key.begin() + 1, key.end());
            j = 0;
        }
        int temp = (ciphertext[i] - key.at(i % keySize));
        temp += 26; // por si acaso es negativo el resultado, en cuyo caso solo hace falta sumar una vez
        temp = temp % 26;
        cleartext += (temp+'a');
        j++;
    }

    return cleartext;
}

int main()
{
    string cleartext = "to be or not to be, that is the question";
    string key = "relations ";

    string ciphertext = encrypt(cleartext, key);
    cout << "Ciphertext: " << ciphertext << endl;
    cleartext = decrypt(ciphertext, key);
    cout << "Cleartext: " << cleartext << endl;

    // realmente no sabia cual era el funcinamiento de t,
    // asi que asumi que era rotar la llave

    cout << "Ahora con el parametro t" << endl;
    cleartext = "there is a secret passage behind the picture frame";
    key = "crypto";
    int t = 3;

    ciphertext = encrypt(cleartext, key, t);
    cout << "Ciphertext: " << ciphertext << endl;
    cleartext = decrypt(ciphertext, key, t);
    cout << "Cleartext: " << cleartext << endl;

    return 0;
}
