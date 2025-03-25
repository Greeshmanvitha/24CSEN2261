Source:CHATGPT


#include <stdio.h>
#include <stdlib.h>

void encryptFile(char *inputFileName, char *outputFileName, int key) {
    FILE *inputFile = fopen(inputFileName, "r");
    FILE *outputFile = fopen(outputFileName, "w");

    if (inputFile == NULL || outputFile == NULL) {
        printf("Error opening files.\n");
        return;
    }

    char ch;
    while ((ch = fgetc(inputFile)) != EOF) {
        fputc(ch + key, outputFile);
    }

    fclose(inputFile);
    fclose(outputFile);
}

void decryptFile(char *inputFileName, char *outputFileName, int key) {
    FILE *inputFile = fopen(inputFileName, "r");
    FILE *outputFile = fopen(outputFileName, "w");

    if (inputFile == NULL || outputFile == NULL) {
        printf("Error opening files.\n");
        return;
    }

    char ch;
    while ((ch = fgetc(inputFile)) != EOF) {
        fputc(ch - key, outputFile);
    }

    fclose(inputFile);
    fclose(outputFile);
}

int main() {
    char inputFileName[] = "original.txt";
    char encryptedFileName[] = "encrypted.txt";
    char decryptedFileName[] = "decrypted.txt";
    int encryptionKey = 5;

    encryptFile(inputFileName, encryptedFileName, encryptionKey);
    printf("File encrypted successfully.\n");

    decryptFile(encryptedFileName, decryptedFileName, encryptionKey);
    printf("File decrypted successfully.\n");

    return 0;
}
