#include <stdio.h>
int main()
{
    int a,b,c,d,e,f,g,h,i,x;

    printf("Enter the order of the determinant ie. 2 or 3: ");
    scanf("%d",&x);

    if (x==2)
    {
        printf("Enter 1st Row Elements: ");
        scanf("%d %d",&a,&b);
        printf("Enter 2nd Row Elements: ");
        scanf("%d %d",&d,&e);
        printf("Determinant is %d",a*e-d*b);

    }
    else if (x==3)
    {
        printf("Enter 1st Row Elements: ");
        scanf("%d %d %d",&a,&b,&c);
        printf("Enter 2nd Row Elements: ");
        scanf("%d %d %d",&d,&e,&f);
        printf("Enter 3rd Row Elements: ");
        scanf("%d %d %d",&g,&h,&i);
        printf("Determinant is %d",a*(i*e-f*h)-b*(d*i-g*f)+c*(d*h-e*g));

    }
    else
    printf("Order more than 3 is not supported.");


return 0;
}
