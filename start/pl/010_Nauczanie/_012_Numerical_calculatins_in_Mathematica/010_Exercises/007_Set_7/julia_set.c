#include "wstp.h"
#include "complex.h"

int juliaSet(double re , double im , int n)
{
	// this is the c constant:
	double complex c = CMPLX(re , im);

	// sending a List to Mathematica,
	// and specifying the number of elements:
	WSPutFunction(stdlink , "List" , 1001); 

	// iteration over the real part:
	for(int ix = 0 ; ix <= 1000 ; ix ++) 
	{
		// the real part:
		double x = 2.0 * (ix - 500.0) / 500.0; 

		//sending another (nested) List to Mathematica:
		WSPutFunction(stdlink , "List" , 1001); 

		// iteration over the imaginary part:
		for(int iy = 0 ; iy <= 1000 ; iy ++) 
		{
			// the imaginary part:
			double y = 2.0 * (iy - 500.0) / 500.0; 
			
			// z_0:
			double complex z = CMPLX(x , y); 

			for(int i = 0 ; i < n ; i++)
			{
				// z_(i + 1):
				z = z * z + c; 	
			}

			// sending the result to mathematica. the real number
			// 1.0 / (1.0 + cabs(z))
			// is small if z is away from 0 and
			// close to 1.0
			// if z is in the vicinity of 0:
			WSPutReal64(stdlink , 1.0 / (1.0 + cabs(z))); 
		}
	}
	return 0;
}

int main(int argc, char *argv[]) 
{
   return WSMain(argc, argv);
}
