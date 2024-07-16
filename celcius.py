def celsius_to_far(celsius):
    F= celsius*(9/5) + 32
    return F

#elsius=input("Enter the temp in celcius: ")
#celsius= float(celsius)
temperatures=[10,-20,-289,100]
for celsius in temperatures:
    if celsius>=-273.5:
        Far= celsius_to_far(celsius)
        print(f"the conversion of {celsius} degrees to  Farenheit is {Far} F")
    elif celsius<-273.5:
        print("not possible lowest temperature is -273.5")

