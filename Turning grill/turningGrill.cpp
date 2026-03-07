#include <iostream>
#include <string> 
#include <vector>
#include <algorithm>
using namespace std;

constexpr bool LEFT = true;
constexpr bool RIGHT = false;
constexpr char PLACEHOLDER = '#';

template <typename T>
void print2DArr(T* ptr, int sizeRow, int sizeCol) {
    for (int i = 0; i < sizeRow; i++) {
        for (int j = 0; j < sizeCol; j++) {
            cout << *(ptr+((i*sizeCol)+j)) << " ";
        }
        cout << endl;
    }
}
template <typename T>
void printArr(T* ptr, int size) {
    for (int j = 0; j < size; j++) {
        cout << *(ptr+j) << " ";
    }
    cout << endl; 
}
template <typename T>
void printVector(const vector<T>& vector1) {
    for (T item : vector1) {
        cout << item << " ";
    }
    cout << endl;
}

string fixText(string text){
    string result = "";
    for (char ch : text) {
        ch = tolower(ch);
        if (ch >= 'a' && ch <= 'z') {
            result += ch;
        }
    }
    return result;
}

void rotate(vector<int>& cutouts, bool rotDirection, int sizeMatrix){
    // printVector(cutouts);
    for (int& num : cutouts){
        int row = num / sizeMatrix; // size es dimension n de la matrix
        int col = num % sizeMatrix;
        int newNum;
        if (rotDirection == RIGHT) {
            newNum = col * sizeMatrix + (sizeMatrix-1-row); // funciona
        } else {
            newNum = (sizeMatrix-1-col)*sizeMatrix + row; 
        }
        num = newNum;
    }
    sort(cutouts.begin(),cutouts.end());
    //printVector(cutouts);
}

bool validateCutouts(vector<int> cutouts, int size) {
    if (cutouts.size()*4 != size*size) { return false; }

    vector<short> count(size*size,0);
    for (int i = 0; i < 4; i++){
        for (int num : cutouts) {
            if (num >= size*size || num < 0) { return false; }
            count[num] = count[num] + 1;
            if (count[num] > 1) { return false; }
        }
        rotate(cutouts, LEFT, size);
    }
    return true;
}

string encrypt(string cleartext, bool rotDirection, int size, vector<int> cutouts){
    if (!validateCutouts(cutouts, size)) {
        throw runtime_error("La llave no es valida");
    }
    
    cleartext = fixText(cleartext);
    string ciphertext(size*size, PLACEHOLDER);
    
    int i = 0;
    int j = 0;
    while (i < cleartext.size()) {  // realizar para todas las letras del texto claro
        if ((i % cutouts.size() == 0) && i!=0){           // rotar cada 4 iteraciones
            rotate(cutouts, rotDirection, size);   // rotar la matriz = cambiar los huecos
            //cout << "Matriz rotada, nuevos huecos en ";
            //printVector(cutouts);
            //cout << i << endl;
            j = 0;                  // resetear posicion inicial para cutouts
        }
        // colocar en posicion del texto cifrado (cutouts) el caracter del texto claro
        ciphertext[cutouts[j]] = cleartext.at(i); // quiza sea necesario hacer una verificacion apra esto
        //printArr(ciphertext, size*size+1);
        i++;
        j++;
    }
    return ciphertext;
}

string decrypt(string ciphertext, bool rotDirection, int size, vector<int> cutouts){
    if (!validateCutouts(cutouts, size)) {
        throw runtime_error("La llave no es valida");
    }
    
    string cleartext(size*size, PLACEHOLDER);
    int i = 0;
    int j = 0;
    while (i < ciphertext.size()) {  // realizar para todas las letras del texto claro
        if ((i % cutouts.size() == 0) && i!=0){           // rotar cada 4 iteraciones
            rotate(cutouts, rotDirection, size);   // rotar la matriz = cambiar los huecos
            // cout << "Matriz rotada, nuevos huecos en ";
            // printVector(cutouts);
            //cout << i << endl;
            j = 0;                  // resetear posicion inicial para cutouts
        }
        cleartext[i] = ciphertext.at(cutouts[j]); // quiza sea necesario hacer una verificacion apra esto
        // printArr(cleartext, size*size+1);
        i++;
        j++;
    }    
    return cleartext;
}

int main() {

    vector<int> huecos = {0, 9, 11, 14}; // si se empiezan a contar los huecos desde la posicion 0;
    string texto;
    string encriptado;

    cout << string(40, '#') << "  PRUEBA 1  " << string(40, '#') << endl;
    texto = "Jim attacks at dawn";
    cout << "Texto original es: " << texto << endl;
    encriptado = encrypt(texto, LEFT, 4, huecos);
    cout << "El texto encriptado es: " + encriptado << endl;
    texto = decrypt(encriptado, LEFT, 4, huecos);
    cout << "El texto claro es: " + texto << endl;

    cout << endl << string(40, '#') << "  PRUEBA 2  " << string(40, '#') << endl;
    texto = "texto";
    cout << "Texto original es: " << texto << endl;
    encriptado = encrypt(texto, LEFT, 4, huecos);
    cout << "El texto encriptado es: " + encriptado << endl;
    texto = decrypt(encriptado, LEFT, 4, huecos);
    cout << "El texto claro es: " + texto << endl;
    
    cout << endl << string(40, '#') << "  PRUEBA 3  " << string(40, '#') << endl;
    huecos = {0,1,2,5,13,17,28,31,33,34,42,43,48,52,54,60,62,69,73,77,81,84,91,92,95}; // si se empiezan a contar los huecos desde la posicion 0
    texto = "this is a message that i am encrypting with a turning grille to provide this illustrative example";
    cout << "Texto original es: " << texto << endl;
    encriptado = encrypt(texto, LEFT, 10, huecos);
    cout << "El texto encriptado es: " + encriptado << endl;
    texto = decrypt(encriptado, LEFT, 10, huecos);
    cout << "El texto claro es: " + texto << endl;
    
    cout << endl << string(40, '#') << "  PRUEBA 4  " << string(40, '#') << endl;
    huecos = {0, 3, 5, 11, 17, 19, 24, 29, 31, 34, 40, 42, 44, 48, 52, 54, 59, 64, 67, 71, 74}; // si se empiezan a contar los huecos desde la posicion 0
    texto = "this is a message that i am encrypting with a turning grille to provide this illustrative example";
    cout << "Texto original es: " << texto << endl;
    encriptado = encrypt(texto, LEFT, 9, huecos);
    cout << "El texto encriptado es: " + encriptado << endl;
    texto = decrypt(encriptado, LEFT, 9, huecos);
    cout << "El texto claro es: " + texto << endl;
    

    
    return 0;
}    
