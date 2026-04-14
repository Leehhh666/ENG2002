"""3D vector library: contains base vector class threeDVec and azimuth-angle subclass vazmAng."""


class threeDVec:
    # Initialize 3D vector components and perform basic input validation.
    def __init__(self,a,b,c):
        try:
            # Convert inputs to float for consistent numeric computation.
            a = float(a)
            b = float(b)
            c = float(c)
        except (TypeError, ValueError):
            # Raise a unified error when inputs are not numeric.
            raise ValueError("a, b, c must be numbers")

        # This assignment requires a to be non-zero, so validate at construction.
        if a == 0:
            raise ValueError("a cannot be zero")

        # Store the three components after validation.
        self.a = a
        self.b = b
        self.c = c

    # Compute squared magnitude: a^2 + b^2 + c^2.
    def magnitude_squared(self):
        magnitude_squared=self.a*self.a+self.b*self.b+self.c*self.c
        return magnitude_squared

    # Compare current vector's squared magnitude with another value `other`.
    # Return convention: 1 (greater), 0 (equal), -1 (smaller).
    def compare_magnitude_squared(self,other):
        m=self.magnitude_squared()
        if m>other:  
            return 1
        elif m==other:
            return 0
        elif m<other:
            return -1


class vazmAng(threeDVec) :
    # Reuse parent initialization and input validation rules from threeDVec.
    def __init__(self,a, b, c):
        super(). __init__ (a,b,c)

    # Approximate azimuth angle using Taylor series of arctan(z), where z = b/a.
    # `terms` is the number of series terms; more terms usually improve accuracy in the convergence interval.
    def get_azimuthal(self,terms):
        ratio=self.b/self.a

        # This assignment constrains z to [-1, 1]; raise an error when out of range.
        if (ratio<=1 and ratio>=-1)== False:
            raise ValueError(f"Invalid ratio b/a={ratio:.6g}: expected in [-1, 1] for arctan series.") 

        # Accumulate terms based on arctan(z)=z-z^3/3+z^5/5-...
        total=0
        for n in range(terms):
            x=2*n+1
            y=1
            for m in range(x):
                y=y*ratio
            if (n%2)==0:
                num=y/x
            elif (n%2)==1:
                num=-y/x
            total=total+num
        return total           
           

if __name__ == "__main__" :
            # Main program: read a, b, c one by one; prompt again on invalid input.
    while True:
        try:
            a = float(input("please enter a: "))
            if a == 0:
                print("a cannot be zero, please input again")
                continue
            break
        except ValueError:
            print("a must be a number")

    while True:
        try:
            b = float(input("please enter b: "))
            break
        except ValueError:
            print("b must be a number")
    while True:
        try:
            c = float(input("please enter c: "))
            break
        except ValueError:
            print("c must be a number")

    # Read Taylor-series term count `terms` (must be an integer).
    while True:
                try:
                    terms=int(input('Please input terms',))  
                    break
                except ValueError:
                    print("terms must be an integer, please input again")  

    # Create object and print the computed azimuth angle.
    vec = vazmAng(a, b, c)
    print(vec.get_azimuthal(terms))

