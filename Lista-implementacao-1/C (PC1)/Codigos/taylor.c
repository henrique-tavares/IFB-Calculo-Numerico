#include <stdio.h>
#include <stdlib.h>
#include <math.h> //necessário usar a flag -lm no momento da compilação

//função que calcula o fatorial de um inteiro
double fatorial(int n);

//função que calcula o valor do polinômio escolhido para um x qualquer
double funcao(int n, double a[], double x);

//função que calcula o valor polinômio de taylor até o índice n, para um x qualquer
//e compara o resultado com o do polinômio original
int funcao_taylor(int n, double at[], double x, double xf);

//função que calcula os coeficientes dos polinomios de taylor
double *vetor_taylor(int n, double *a);

int main()
{
    int n, qtd;
    double *a, *at, *x, xf, xt;

    scanf("%i", &n); //lendo o grau do polinômio
    getchar();

    a = malloc((n + 1) * sizeof(double));

    for (int i = 0; i <= n; i++)
    {
        scanf("%lf", &a[i]); //lendo os coeficientes do polinômio
        getchar();
    }

    at = vetor_taylor(n, a);

    scanf("%i", &qtd); //lendo a quantidade de "x" que serão calculados
    getchar();

    x = malloc(qtd * sizeof(double));

    for (int i = 0; i < qtd; i++)
    {
        scanf("%lf", &x[i]); //lendo os "x"
        getchar();
    }

    putchar('\n');
    for (int i = 0; i < qtd; i++)
    {
        xf = funcao(n, a, x[i]); //calculando o valor do polinomio para os "x"

        funcao_taylor(n, at, x[i], xf); //calculando os valores dos polinomios de taylor e comparando-os com o valor do polinômio original

        putchar('\n');
    }

    return 0;
}

double fatorial(int n)
{
    return (n > 1) ? n * fatorial(n - 1) : 1;
}

double funcao(int n, double a[], double x)
{
    double soma = 0;

    for (int i = 0; i <= n; i++)
    {
        soma += a[i] * pow(x, i); //calculando o valor do polinômio
    }

    return soma; // retornando o valor calculado
}

int funcao_taylor(int n, double *at, double x, double xf)
{
    double soma = 0;

    for (int i = 0; i <= n; i++)
    {
        soma += (at[i] * pow(x, i)) / fatorial(i); //calculando os polinomios de taylor de indice i + 1

        printf("%i %lf %lf\n", i + 1, soma, xf); //printando o indice e os valores do poloinômio de taylor e do polinômio original

        if (fabs(soma - xf) <= 0.001) //comparando a precisão do polinômio de taylor
            return 0;
    }

    return 0;
}

double *vetor_taylor(int n, double *a)
{
    double *at = malloc((n + 1) * sizeof(double));

    for (int i = 0; i <= n; i++)
    {
        at[i] = a[i]; //copiando os coeficientes para um outro vetor
    }

    for (int i = 0; i <= n; i++)
    {
        at[i] *= fatorial(i); //multiplicando os coeficientes pelos fatoriais de seus graus
    }

    return at;
}