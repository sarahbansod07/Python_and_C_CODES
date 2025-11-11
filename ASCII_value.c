#include<stdio.h>
int main()

{
    char ch;
    printf("Enter a character:"); 
    scanf("%c", &ch);  //character input from user 

    printf("You entered %c", ch); // character will be displayed

    printf("The ASCII value is: %d", ch); //ASCII value will be displayed 

    return 0;

}