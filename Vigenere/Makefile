
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -fsanitize=address,undefined -g -std=c++17
TARGET = vigenere

$(TARGET): vigenere.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) vigenere.cpp

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)
