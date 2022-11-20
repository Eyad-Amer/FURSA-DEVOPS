# Write a bash script that reads a temperature in Fahrenheit and converts
# it to Celcius

echo "please enter a temptemp in Fahrenheit:"
read fahrenheit
#celsius = (fahrenheit - 32)*5/9
celsius=$((($fahrenheit-32)*5/9))
echo "The temptemp in celsius: $celsius"
