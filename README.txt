# jetbrains-credit-calculator
About
Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us.
Learning outcomes
You’ll learn how to use mathematics and Python in everyday tasks, use third-party modules and libraries. Also, you’ll learn more about different financial instruments. Finally, you will make your own credit calculator!

# Work on project. Stage 1/4: Beginning
# https://hyperskill.org/projects/90/stages/500/implement

"""
Description
Let's stop and think for a second: what should a basic credit calculator do? In general, it is supposed to take several parameters such as credit principal and credit interest, calculate the needed values (for example, monthly payment or overpayment), and output them.

If you are not familiar with these financial concepts, don't worry! We'll explain them in simpler terms. A principal is the original amount of money you get on credit. An interest is the charge you pay for borrowing money, usually calculated as a percentage of the loan sum.

Objective
Let's start by imitating this basic behavior. There are some prepared variables in the source code that are ready for use: these are the text messages that our credit calculator could output. At this stage, all you need to do is output them in the right order.

Example
Output:

Credit principal: 1000
Month 1: paid out 250
Month 2: paid out 250
Month 3: paid out 500
The credit has been repaid!
"""

# Work on project. Stage 2/4: Dreamworld
# https://hyperskill.org/projects/90/stages/501/implement
"""
Description
If you found the previous stage too easy, let's move on to something more interesting. The best credits are probably those with a 0% interest; such credits are called installments.

Let's make some calculations for the installments. The user might know the number of periods (months) and want to calculate the monthly payment. Or, the user might know the amount of monthly payment and wonder how many periods it would take to repay the installments.

At this stage, the user should be prompted to input the credit principal. Then, the user should indicate what needs to be calculated (the monthly payment or the number of months) and enter the necessary parameter. After that, the credit calculator should calculate and output the value that the user wants to know.

Not all the resulting numbers will be neat and round. Let’s assume that we don't care about the digits after the dot. If you get a floating-point expression as a result of the calculation, you’ll have to take some additional steps. Take a look at Example 4 in the section "Examples". There, you need to calculate the monthly payment. You know that the credit principal is 1000 and you want to pay it in 9 months. The payment can be calculated like this:

payment = principal / months=\dfrac{1000}{9} = 1000 / 9 =111.11...

Of course, you can’t pay that exact amount of money. You'll have to round it up and make it 112. Remember that no payment can be more than a monthly payment. If you make a monthly payment of 111, the last payment will be 112, and if you make a monthly payment of 112, the last payment will be 104, which is okay by the rules. You can calculate the last payment with this formula:

lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104

At this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display both the monthly payment and the last payment.

Objectives
Your program should do the following:

Prompt the user to enter their credit principal and choose one of the two parameters: a number of months or a monthly payment;
Ask for the missing value to perform further calculations;
Finally, output the results.
Examples
The greater-than symbol followed by a space (> ) represent user input. Note that these are not part of the input.

Example 1:

Enter the credit principal:
> 1000
What do you want to calculate?
type "m" - for the number of months,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It takes 7 months to repay the credit
Example 2:

Enter the credit principal:
> 1000
What do you want to calculate? 
type "m" for the number of months,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It takes 1 month to repay the credit
Example 3:

Enter the credit principal:
> 1000
What do you want to calculate?
type "m" for the number of months, 
type "p" for the monthly payment:
> p
Enter the count of months:
> 10

Your monthly payment = 100
Example 4:

Enter the credit principal:
> 1000
What do you want to calculate?
type "m" for the number of months,
type "p" for the monthly payment
> p
Enter the number of months:
> 9

Your monthly payment = 112 with last monthly payment = 104.
"""

# Work on project. Stage 3/4: Annuity payment
# https://hyperskill.org/projects/90/stages/502/implement

"""
Description
Let's compute all the parameters of the credit. There are at least two kinds of credit loans: those with annuity payment and those with differentiated payment. At this stage, you're going to calculate only the annuity payment that is fixed during the whole credit term.

Here is the formula:

A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}A 
ordinary_annuity
​	
 =P∗ 
(1+i) 
n
 −1
i∗(1+i) 
n
 
​	
 

Where:

AA = annuity payment;

PP = credit principal;

ii = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;

nn = number of payments. Usually, it’s the number of months.

You are interested in four values: the number of periods to repay the credit loan, the monthly payment, the credit principal, and the credit interest. Each of these values can be calculated if the others are known:

Credit principal:

P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}P= 
( 
(1+i) 
n
 −1
i∗(1+i) 
n
 
​	
 )
A
​	
 

A number of payments:

n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)n=log 
1+i
​	
 ( 
A−i∗P
A
​	
 )

Objectives
At this stage, you should add new functionality to your calculator:

First, prompt the user for the parameter they want to calculate. The calculator should be able to calculate the number of periods, the monthly payments, and the credit principal;
Then, prompt the user to input the remaining values;
Finally, compute and output the value that they wanted.
Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.
Please be accurate when converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

Note that at this stage you have to ask the user to input the parameters in a predetermined order provided below. Simply disregard the value that the user wants to calculate and follow the rest of the list. For example, it can be the monthly payment if the user typed “a” as an answer to the question “What do you want to calculate?”. Here is the order:

The first is the credit principal;

The second is a monthly payment;

The next is a number of periods;

The last is an interest rate.

Examples
The greater-than symbol followed by a space (> ) represent the user input. Note that these are not part of the input.

Example 1:

What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:
> n
Enter the credit principal:
> 1000000
Enter the monthly payment:
> 15000
Enter the credit interest:
> 10
You need 8 years and 2 months to repay this credit!
Let’s take a closer look at Example 1.

You know the credit principal and the credit interest, and you want to calculate the number of months. What should you do?

1) You need to know the nominal interest rate. It is calculated like this:

i = \dfrac{10\%}{12 * 100\%} = 0.008333...i= 
12∗100%
10%
​	
 =0.008333...

2) Now you can calculate the count of periods:

n = \log_{1 + 0.008333...} \left( \dfrac{15000}{15000-0.008333... * 1000000} \right) = 97.71...n=log 
1+0.008333...
​	
 ( 
15000−0.008333...∗1000000
15000
​	
 )=97.71...

3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and for 98th month the user will pay 0.71... of the monthly payment. So, there are 98 months to pay.

n = 98n=98

4) Finally, you need to convert “98 months” to “8 years and 2 months”, so it is more readable and understandable for the user.

Consider other examples:

Example 2:

What do you want to calculate? 
type "n" for the number of months, 
type "a" for the annuity monthly payment,
type "p" for the credit principal: 
> a
Enter the credit principal: 
> 1000000
Enter the number of periods:
> 60
Enter the credit interest:
> 10
Your annuity payment = 21248!
Example 3:

What do you want to calculate?
type "n" for the number of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:
> p
Enter the annuity payment:
> 8721.8
Enter the count of periods:
> 120
Enter the credit interest:
> 5.6
Your credit principal = 800000!
"""

# Work on project. Stage 4/4: Differentiate payment
# https://hyperskill.org/projects/90/stages/503/implement

"""
Description
Finally, let's add the ability to compute differentiated payment. This is a kind of payment where the part for reducing the credit principal is constant. Another part of the payment is for interest repayment and it reduces during the credit term. It means that the payment is different every month. Let’s look at the formula:

Dm = P / n + i * (P - P * (m-1) / n )

Where:

Dm = mth differentiated payment;

P = credit principal;

i = nominal interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01;

n = number of payments (months);

m = current period.

As you can see, the user has to input a lot of parameters. So, it might be convenient to use command-line arguments.

Suppose you used to run your credit calculator via a command line like this:

python creditcalc.py
Using command-line arguments, you can run your program this way:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
In that case, your program can get different values without asking the user to input them. It can be useful when you are developing your program and trying to find a mistake, so you run the program again and again with the same parameters. Also, it's convenient if you made a mistake in a single parameter. You don't have to input all other values again.

To confidently work with command-line arguments in Python, check out this tutorial.

Objectives
In this stage, you need to implement the following features:

Calculating differentiated payment. To do this, the user may run the program specifying the interest, the number of periods, and the credit principal.
The ability to calculate the same values as in the previous stage for annuity payment (principal, count of periods, and the value of payment). The user specifies all the known parameters using command-line arguments, so there will be one unknown parameter. This is the value that the user wants to calculate.

Handling invalid parameters. It's a good idea to show an error message Incorrect parameters if the parameters are invalid.

The final version of your program is supposed to work from the command line and parse the following parameters:

--type, which indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff", or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment, which refers to the monthly payment. For --type=diff, the payment is different each month, so we cannot calculate a number of periods or the principal, therefore, its combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculating both types of payment. You can get its value knowing the interest, the annuity payment, and the number of periods.
--periods parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment, and the principal.
--interest is specified without the percentage sign. Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, so these parameters are incorrect:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
You might have noticed that for differentiated payments you need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (missing either a number of periods, the payment, or the principal). Thus, when less than four parameters are given, you should display the error message:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
Another case when you should output this message is with negative values. We can't work with these!

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
Finally, don't forget to compute the value of overpayment, and you'll have your real functional credit calculator!

Examples
The greater-than symbol followed by a space (> ) represent the user input. Note that these are not part of the input.

Example 1: calculating differentiated payments

> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: paid out 108334
Month 2: paid out 107500
Month 3: paid out 106667
Month 4: paid out 105834
Month 5: paid out 105000
Month 6: paid out 104167
Month 7: paid out 103334
Month 8: paid out 102500
Month 9: paid out 101667
Month 10: paid out 100834

Overpayment = 45837
In this example, the user wants to take a credit loan with differentiated payments. You know the principal, the number of periods, and the interest rate, which are 1,000,000, 10 months, and 10%, respectively.

The calculator should calculate the payments for all 10 months. Let’s use the formula mentioned above. In this case:

P = 1000000
n = 10
i =interest / (12 * 100\%) = 10\%  / (12 * 100\%) = 0.008333...

Then, let’s find the payment for the first month (m=1):

D1 = P / n + i * (P - P * (m-1) / n ) = 1000000 / 10 + 0.008333... * ( 1000000 - 1000000 *(1-1) / 10 ) = 108333.333...

The second month (m = 2):

D2 = P / n + i * (P - P * (m-1) / n ) = 1000000 / 10 + 0.008333... * ( 1000000 - 1000000 *(2-1) / 10 ) = 107500

The third month (m = 3):

D2 = P / n + i * (P - P * (m-1) / n ) = 1000000 / 10 + 0.008333... * ( 1000000 - 1000000 *(3-1) / 10 ) = 106666.666...

And so on. You can see other monthly payments above.

Your credit calculator should output monthly payments for every month like in the first stage. Also, don't forget to round up the floating-point values.
Finally, your credit calculator should add up all the payments and subtract the credit principal so that you get the overpayment.

Example 2: finding the annuity payment for the 60-month (or 5-year) credit loan with the principal 1,000,000 and a 10% interest

> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
Example 3: less than four arguments are given

> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
Example 4: calculating differentiated payments given the principal 500,000, the period of 8 months, and an interest rate of 7.8%

> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: paid out 65750
Month 2: paid out 65344
Month 3: paid out 64938
Month 4: paid out 64532
Month 5: paid out 64125
Month 6: paid out 63719
Month 7: paid out 63313
Month 8: paid out 62907

Overpayment = 14628
Example 5: calculating the principal for an individual paying 8,722 per month for 120 months (10 years) with an interest rate of 5.6%

> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your credit principal = 800018!
Overpayment = 246622
Example 6: figuring out how much time an individual needs to repay the credit loan with the principal 500,000, the monthly payment of 23,000 at a 7.8% interest rate

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
You need 2 years to repay this credit!
Overpayment = 52000

"""

