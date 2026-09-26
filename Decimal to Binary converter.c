#include <stdio.h>
int main()
{
    int decimal,quo,binary,remainder,numbers[8],i=7;
    printf("DECIMAL TO 8-BIT BINARY CONVERTER\n");
    printf("Enter the decimal number: ");
    scanf("%d",&decimal);

    if (decimal>255)
    printf("This number cannot be converted into 8-bits binary\n");

    else
    {
    while (decimal>=1)
    {
        remainder=decimal%2;
        decimal=decimal/2;
        
        numbers[i]=remainder;
        i--;
    }

    while (i>=0)
    {numbers[i]=0;
    i--;}

    for (int i=0;i<=7;i++)
    {printf("%d",numbers[i]);}
    }

return 0;
}
