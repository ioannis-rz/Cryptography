#include <iostream>
#include <string> 
#include <vector>
using namespace std;

constexpr bool LEFT = true;
constexpr bool RIGHT = false;

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

vector<int> rotate(vector<int>& holes, bool rotDirection){
    
    return holes;
}

string encrypt(string cleartext, bool rotDirection, int size, vector<int> holes){
    char* ciphertext = new char[(size*size)+1];
    ciphertext[size*size] = '\0';
    
    for (int i = 0; i < size*size; i++) {
        ciphertext[i] = '^';
    }
    
    //ciphertext.reserve(16); // para ejemplo, reserva tamano 16
    //int* arr = new int[size * size];
    int i = 0;
    while (i < 4) {
        // colocar en posicion del texto cifrado (holes) el caracter del texto claro
        ciphertext[holes[i]] = cleartext.at(i); // quiza sea necesario hacer una verificacion apra esto
        rotate(holes, rotDirection); // rotar la matriz = cambiar los huecos
        i++;
    }
    
    // printArr(ciphertext, size*size);
    
    string s = ciphertext;
    cout << s << endl;
    return s;
}

string decrypt(string ciphertext, bool rotDirection, int size, vector<int> holes){
    string cleartext = "";

    return cleartext;
}

int main() {
    cout << "Hello World" << endl;
    vector<int> huecos = {0, 9, 11, 14}; // si se empiezan a contar los huecos desde la posicion 0
    string texto = encrypt("jimattacksatdawn", LEFT, 4, huecos);
    cout << "El texto encriptado es: " + texto << endl;
    return 0;
}