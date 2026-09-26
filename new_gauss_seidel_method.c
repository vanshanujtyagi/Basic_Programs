#include <stdio.h>
int main()
{
    float x,y,z;
    int a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3,n,i;
    printf("Please ensure equations are diagonally dominant.\n");
    printf("Enter the first equation : ");
    scanf("%d%d%d%d",&a1,&b1,&c1,&d1);
    printf("Enter the second equation : ");
    scanf("%d%d%d%d",&a2,&b2,&c2,&d2);
    printf("Enter the third equation : ");
    scanf("%d%d%d%d",&a3,&b3,&c3,&d3);
    printf("Select the number of ITERATIONS : ");
    scanf("%d",&n);

    printf("%dx+%dy+%dz=%d\n",a1,b1,c1,d1);
    printf("%dx+%dy+%dz=%d\n",a2,b2,c2,d2);
    printf("%dx+%dy+%dz=%d\n",a3,b3,c3,d3);

    for (i=1;i<=n;i++)
    {
        if (i==1)
        {printf("Iteration %d:",i);
        x=(float)d1/a1;
        y=((float)d2-a2*x)/b2;
        z=((float)d3-a3*x-b3*y)/c3;
        printf("x=%f, y=%f, z=%f\n",x,y,z);}
    
        else
        {printf("Iteration %d:",i);
        x=((float)d1-b1*y-c1*z)/a1;
        y=((float)d2-a2*x-c2*z)/b2;
        z=((float)d3-a3*x-b3*y)/c3;
        printf("x=%f, y=%f, z=%f\n",x,y,z);
        }
    }
    printf("Approximate Solutions are x=%f, y=%f, z=%f",x,y,z);

return 0;
}