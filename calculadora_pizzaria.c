#include <stdio.h>

//Programa para calcular desconto e valor por pessoa em uma compra

int main(){
    float bruto = 0;
    float desconto = 0;
    float liquido = 0;
    int pessoas = 0;

    printf("\n Insira o valor da compra: ");
    scanf("%f", &bruto);
    printf("\n Insira o desconto (em porcentagem): ");
    scanf("%f", &desconto);
    printf("\n Insira o numero de pessoas: ");
    scanf("%d", &pessoas);
    liquido = bruto - bruto * (desconto/100);
    printf("\n O valor total com desconto e %.0f reais", liquido);
    printf("\n O valor por pessoa e %.0f reais", liquido/pessoas);

    return 0;
}