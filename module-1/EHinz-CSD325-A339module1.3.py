print('Welcome to my Module 1.3 Program!')
print('Created by Elizabeth Hinz for CSD325:A339!')

# This program uses a recursive function to count 
# down the 100 bottles of beer on the wall song

def print_recursive(n):
    # If n is greater than 0, continue the song with countdown. 
    if n>0:
        print(f'{n} bottles of beer on the wall, {n} bottles of beer.')
        print(f'Take one down and pass it around,', end="")
        # Subtract one from the bottles from the base case the continue song
        if n -1 > 0:
            print(f' {n-1} bottles of beer on the wall.')
        # Stop countdown if no more bottles left
        else:
          print('No more bottles of beer on the wall.')
        # Output bottles minus previous amount
        print_recursive(n-1)
    else:
          print('No more bottles of beer on the wall.')
          print('Time to buy some more bottles of beer.')
    
# Set main function
def main():
    while True:
        try: 
            # Prompt user for beer number
            n=int(input('Enter number of beers: '))
            if n>0:
                # Start recursive function
                print_recursive(n)
                break
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invald input. Please enter a positive integer.')
# Run main function
main()
