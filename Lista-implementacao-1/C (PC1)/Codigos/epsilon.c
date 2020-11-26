#include <stdio.h>

int main()
{
    float epsilon = 1;    //variável de precisão simples
    double d_epsilon = 1; //variável de precisão dupla

    //loop para encontrar o menor número de precisão simples
    while (epsilon + 1 > 1)
    {
        epsilon /= 2;
    }

    //loop para encontrar o menor número de precisão dupla
    while (d_epsilon + 1 > 1)
    {
        d_epsilon /= 2;
    }

    printf("%e\n%e\n", epsilon, d_epsilon); //printando os resultados

    return 0;
}