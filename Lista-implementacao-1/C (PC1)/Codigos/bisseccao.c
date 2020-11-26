#include <stdio.h>
#include <stdlib.h>
#include <math.h> //necessário usar a flag -lm no momento da compilação
#define iteracoes 10000

typedef struct func
{
    int grau;
    double *coef;
    double (*calcula)(int, double *, double);

} func_t;

//função que calcula o valor do polinômio escolhido para um x qualquer
double f_de_x(int n, double *a, double x);

int main()
{
    func_t f;
    f.calcula = f_de_x;

    double l, r, m;

    scanf("%i", &f.grau); //lendo o grau do polinômio
    getchar();

    f.coef = malloc((f.grau + 1) * sizeof(double));

    for (int i = 0; i <= f.grau; i++)
    {
        scanf("%lf", &f.coef[i]); //lendo os coeficientes do polinômio
        getchar();
    }

    scanf("%lf", &l); //lendo o ponto incial do intervalo
    getchar();
    scanf("%lf", &r); //lendo o ponto final do intervalo
    getchar();

    for (long int i = 0; i <= iteracoes; i++)
    {
        m = l + ((r - l) / 2);

        if (fabs(f.calcula(f.grau, f.coef, m)) <= 0.0001) //comparando a precisão da raiz
        {
            printf("\n%lf\n\n", m); //printando a raiz encontrada
            return 0;
        }

        if ((f.calcula(f.grau, f.coef, m) * f.calcula(f.grau, f.coef, l)) < 0) //verificando se a raiz está na segunda metade do intervalo
        {
            r = m; //atualizando o ponto final do intervalo de acordo com a condição acima
        }

        else //caso a raiz não esteja na segunda metade do intervalo
        {
            l = m; //atualizando o ponto inicial do intervalo de acordo com a condição acima
        }

        if (i == iteracoes)
        {
            printf("raiz nao encontrada\n"); //caso a raiz não seja encontrada
        }
    }

    return 0;
}

double f_de_x(int n, double *a, double x)
{
    double soma = 0;

    for (int i = 0; i <= n; i++)
    {
        soma += a[i] * pow(x, i); //calculando o valor do polinômio
    }

    return soma; //retornando o valor calculado
}