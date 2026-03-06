#include <iostream>
#include <string> 
#include <vector>
#include <algorithm>
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
template <typename T>
void printVector(const vector<T>& vector1) {
    for (T item : vector1) {
        cout << item << " ";
    }
    cout << endl;
}

vector<int> rotate(vector<int>& holes, bool rotDirection, int sizeMatrix){
    // printVector(holes);
    for (int& num : holes){
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
    sort(holes.begin(),holes.end());
    //printVector(holes);
    return holes;
}

string encrypt(string cleartext, bool rotDirection, int size, vector<int> holes){
    char* ciphertext = new char[(size*size)+1];
    ciphertext[size*size] = '\0';
    
    for (int i = 0; i < size*size; i++) {
        ciphertext[i] = 'x';
    }
    
    int i = 0;
    int j = 0;
    while (i < cleartext.size()) { // realizar para todas las letras del texto claro
        if ((i % holes.size() == 0) && i!=0){ // rotar cadd 4 iteraciones
            holes = rotate(holes, rotDirection, size); // rotar la matriz = cambiar los huecos
            cout << "Executed rotation, nuevos huecos en ";
            printVector(holes);
            //cout << i << endl;
            j = 0; // resetear posicion inicial para holes
        }
        // colocar en posicion del texto cifrado (holes) el caracter del texto claro
        ciphertext[holes[j]] = cleartext.at(i); // quiza sea necesario hacer una verificacion apra esto
        printArr(ciphertext, size*size+1);
        i++;
        j++;
    }

    // printArr(ciphertext, size*size);
    string s = ciphertext;
    return s;
}

string decrypt(string ciphertext, bool rotDirection, int size, vector<int> holes){
    string cleartext = "";

    return cleartext;
}

int main() {
    cout << "Hello World" << endl;
    vector<int> huecos = {0, 9, 11, 14}; // si se empiezan a contar los huecos desde la posicion 0
    string texto = encrypt("jimattackatdawn", LEFT, 4, huecos);
    cout << "El texto encriptado es: " + texto << endl;
    return 0;
}