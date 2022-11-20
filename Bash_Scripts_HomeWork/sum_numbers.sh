
# Write a bash script that collects two numbers from the user and then
# prints a message if these two numbers are smaller or greater than 100.

echo "please enter the first number:"
read n1
echo "please enter the secund number:"
read n2
sum=$(($n1+$n2))
if [ $sum -gt 100 ]
then
	echo "The sum of the numbers is greaten then 100"
elif [ $sum -lt 100 ]
then
	echo "The sum of the numbers is smaller then 100"
else
	echo "The sum of the numbers is equal to 100"
fi
