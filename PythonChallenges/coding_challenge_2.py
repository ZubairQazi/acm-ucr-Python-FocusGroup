def main():
   # Multiply the values in this array by a value that is inputted by the user
   arr = [1, 2, 4, 6, 8, 10]
   inputNum = int(input("Please enter a value to multiply an array by: "))
   for i in arr:
       i *= inputNum
       print(i)

if __name__ == "__main__":
   main()

'''
Please enter a value to multiply an array by: 5
5
10
20
30
40
50
'''
