#Jayden
# Nov 7 2023
#A program that uses functions to print out months.
#Modified by:  Jayden

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

     monthNum = int(input("Enter a number"))

    if monthNum == 1:
      return ("january")
      monthString = monthString + "january" 
    elif monthNum == 2:
      return ("february")
      monthString = monthString + "february" 
    elif monthNum == 3:
      return ("march")
      monthString = monthString + "march" 
    elif monthNum == 4:
        return ("april")
        monthString = monthString + "april" 
    elif monthNum == 5:
        return ("may")
        monthString = monthString + "may" 
    elif monthNum == 6:
        return ("june")
        monthString = monthString + "june" 
    elif monthNum == 7:
        return ("july")
        monthString = monthString + "july" 
    elif monthNum == 8:
        return ("august")
        monthString = monthString + "august" 
    elif monthNum == 9:
        return ("september")
        monthString = monthString + "september" 
    elif monthNum == 10:
        return ("october")
        monthString = monthString + "october" 
    elif monthNum == 11:
        return ("november")
        monthString = monthString + "november" 
    elif monthNum == 12:
        return ("december")
        monthString = monthString + "december" 
    else:
        return ("hello!")
        monthString = monthString + "hello" 


    return(monthString)

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
