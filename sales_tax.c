/* Title: Understand and implement basic concepts of C

Name: Sarah Nitin Bansod
Div: C
Roll No.: 03 */

#include<stdio.h> //header file
int main()     //main function, the prg execution starts from here
{
    float Printed_price, x, y; //floating type input variables 
    float discount,Discounted_Amt,Tax, Final_amt; //floating type processing/output variables

    printf("Enter Printed Price:");  //taking input from user
    scanf("%d", &Printed_price);

    printf("Enter val of x:");      //% discount on commodity,taking input from user
    scanf("%d", &x);

    printf("Enter val for y:");    //sales_tax_on_commodity,taking input from user
    scanf("%d", &y);

    discount= (Printed_price*x)/100;
    printf("the discount is:%f",discount);  //calculating discount on the commodity
    
    Discounted_Amt = Printed_price -discount;
    printf("the discounted amount is:", Discounted_Amt);   //calculating discounted amt

    Tax = (Discounted_Amt*y)/100;    //calculating sales tax
    printf("the sales tax is:",Tax); 

    Final_amt = Discounted_Amt + Tax;
    printf("the final amount is:%f", Final_amt); // calculating final amount of the commodity
   
    return 0;

}
    