CC = g++  # Changed from CC = c++ for typical g++ compiler
EXEC = spider
SRC = main.cpp
OBJ = $(SRC:.cpp=.o)
HOME = $(shell pwd)
CURL_INCLUDE = $(HOME)/curl/include
CURL_LIB = $(HOME)/curl/lib

# Compiler and linker flags
CXXFLAGS = -Wall -I$(CURL_INCLUDE)
LDFLAGS = -L$(CURL_LIB) -lcurl

all: $(EXEC)

$(EXEC): $(OBJ)
	cmake ./curl/
	make ./curl/
	$(CC) -o $(EXEC) $(OBJ) $(LDFLAGS)

%.o: %.cpp
	$(CC) $(CXXFLAGS) -c $< -o $@

clean:

	rm -f $(OBJ) $(EXEC)
