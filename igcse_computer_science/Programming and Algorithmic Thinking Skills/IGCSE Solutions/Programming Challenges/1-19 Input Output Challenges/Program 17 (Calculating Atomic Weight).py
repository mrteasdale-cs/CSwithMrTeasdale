## Calculating the Atomic Weight of Hydrocarbons (Alkanes)
## Program 17
## With Comments

## The user is only asked for a single input this time.

carbon = int(input("Enter the number of carbon atoms?"))

## The program uses the number of Carbon atoms to calculate the
## number of Hydrogen Atoms and the Atomic Weight of the molecule.
## These two values should be calculated and stored.

hydrogen = (carbon*2) + 2
atomicWeight = carbon*12 + hydrogen

## The three stored values (carbon, hydrogen & atomicWeight) can now
## be used in a single, complex print() statement to produce the output.

print("The atomic mass of C"+str(carbon)+"H"+str(hydrogen),"is",atomicWeight)

## NOTE
## To create an output that combines strings and integers we must use the
## string function, str(), to convert the integers to strings first.  This is
## because Python will only concatenate strings.  Without the str() functions
## in the above code, running the program would produce an error message.