%{

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h> 

#if YYBISON
int yylex();
int yyerror();
#endif

/* Structure pour gérer la chaîne et sa taille actuelle*/
typedef struct {
    char* data;
    size_t size;
} StringBuffer;

void initBuffer(StringBuffer* buffer) {
    buffer->data = NULL;
    buffer->size = 0;
}

/* Fonction pour ajouter une chaîne au buffer */
void appendString(StringBuffer* buffer, const char* str) {
    size_t len = strlen(str);
    buffer->data = realloc(buffer->data, buffer->size + len + 1);
    if (buffer->data == NULL) {
        exit(EXIT_FAILURE);
    }
    strcpy(buffer->data + buffer->size, str);
    buffer->size += len;
}

/* Fonction pour concaténer des chaînes */
char* conc(int count, ...) {
    va_list args;
    int totalLength = 0;

    /* Calculer la longueur totale nécessaire pour la chaîne concaténée */
    va_start(args, count);
    for (int i = 0; i < count; i++) {
        const char* str = va_arg(args, const char*);
        totalLength += strlen(str);
    }
    va_end(args);

    /* Allouer de la mémoire pour la chaîne concaténée */
    char* result = (char*)malloc((totalLength + 1) * sizeof(char));
    if (result == NULL) {
        /* Gestion d'erreur si l'allocation échoue */
        exit(EXIT_FAILURE);
    }
    result[0] = '\0';

    /* Concaténer les chaînes */
    va_start(args, count);
    for (int i = 0; i < count; i++) {
        const char* str = va_arg(args, const char*);
        strcat(result, str);
    }
    va_end(args);

    return result;
}

/* Fonction d'écriture d'un buffer dans le fichier main.py */
void write(const StringBuffer* buffer) {
    FILE *f = fopen("main.py", "w");
    if (f == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        exit(EXIT_FAILURE);
    }
    fprintf(f, "%s", buffer->data);
    fclose(f);
}

int cnt;
StringBuffer debut;
StringBuffer fin;

%}

%union
{
    char *lettre;
};

/* tokens */
%token INSTRUCTION
%token FDL
%token VIRG
%token NUMB

%left FDL

%type <lettre> INSTRUCTION programme input NUMB

%%
contenu:
        input FDL programme         { ; }
    ;
input:
    INSTRUCTION                     { appendString(&debut, conc(3, "input = [", $1, "]\n\nprogramme = [\n")); }
    ;
programme:
        INSTRUCTION                 { appendString(&debut, conc(3, "'", $1, "',\n")); }
    |   programme FDL programme     { ; }
    ;
%%

int main() {
    appendString(&debut, "from machine_RAM import *\n\n");
    appendString(&fin, "]\n\nram = machine(programme, input)\n\nram.calcule()\n");

    yyparse();
    
    /* Concaténation des deux Buffers */
    debut.data = realloc(debut.data, debut.size + fin.size + 1);
    strcat(debut.data, fin.data);
    debut.size += fin.size;

    write(&debut);
    
    free(debut.data);
    free(fin.data);

}