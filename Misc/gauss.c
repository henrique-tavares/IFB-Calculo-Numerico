#include <stdio.h>

void swap(double a[], double b[], int n, double *vet1, double *vet2, int *x1, int *x2);
void gauss(double matriz[10][10], double vet[], int x[], int m, int n);
void jordan(double matriz[10][10], double vet[], int m, int n);

int main()
{
    double matriz[10][10], vet[10];
    int x[10];
    int m, n; // m = linhas, n = colunas.

    scanf("%i", &m);
    getchar();
    scanf("%i", &n);
    getchar();

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (j == n)
            {
                scanf("%lf", &vet[i]);
                x[i] = i + 1;
                getchar();
            }
            else
            {
                scanf("%lf", &matriz[i][j]);
                getchar();
            }
        }
    }

    gauss(matriz, vet, x, m, n);
    jordan(matriz, vet, m, n);

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (j == n)
                printf("| %10lf", vet[i]);
            else
                printf("%10lf ", matriz[i][j]);
        }
        putchar('\n');
    }
    putchar('\n');

    for (int i = 0; i < n; i++)
    {
        printf("x%i = %lf\n", x[i], vet[i]);
    }

    return 0;
}

void gauss(double matriz[10][10], double vet[], int x[], int m, int n)
{
    double l;

    for (int i = 0; i < m - 1; i++)
    {
        for (int k = i + 1; k < m; k++)
        {
            if (matriz[i][i] == 0)
            {
                for (int j = i; j < m; j++)
                {
                    if (matriz[j][i] != 0)
                        swap(matriz[j], matriz[i], n, &vet[j], &vet[i], &x[j], &x[i]);
                }
            }
            if (matriz[i][i] != 0)
            {
                l = -(matriz[k][i] / matriz[i][i]);
                for (int j = i; j <= n; j++)
                {
                    if (j == n)
                        vet[k] += l * vet[i];
                    else
                        matriz[k][j] += l * matriz[i][j];
                }
            }
        }
    }
}

void jordan(double matriz[10][10], double vet[], int m, int n)
{
    double l;

    for (int i = m - 1; i >= 0; i--)
    {
        vet[i] /= matriz[i][i];
        matriz[i][i] /= matriz[i][i];

        for (int k = i - 1; k >= 0; k--)
        {
            if (matriz[i][i] != 0)
            {
                l = -(matriz[k][i] / matriz[i][i]);
                for (int j = n; j >= 0; j--)
                {
                    if (j == n)
                        vet[k] += l * vet[i];
                    else
                        matriz[k][j] += l * matriz[i][j];
                }
            }
        }
    }
}

void swap(double a[], double b[], int n, double *vet1, double *vet2, int *x1, int *x2)
{
    double aux;
    int aux2;

    for (int i = 0; i <= n; i++)
    {
        if (i == n)
        {
            aux = *vet1;
            *vet1 = *vet2;
            *vet2 = aux;

            aux2 = *x1;
            *x1 = *x2;
            *x2 = aux2;
        }
        else
        {
            aux = a[i];
            a[i] = b[i];
            b[i] = aux;
        }
    }
}