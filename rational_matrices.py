import math
import random

# The fractions module provides support for rational number arithmetic.
from fractions import Fraction

import numpy as np

################################################################################
####################################################################################
    ###### Methods for Qmatrix #####

# TO DO: Maybe this should be a class?
# --------------------------------------------

def printQmtx(M):
    """ Pretty print of matrix M """
    print('(' , M[0,0],'   ', M[0,1], ')')
    print('(' , M[1,0],'   ', M[1,1], ')')
    return    
# --------------------------------------------

def det(M):
    """ Returns determinant of matrix M """
    return M[0,0]*M[1,1]-M[1,0]*M[0,1]
# --------------------------------------------

def tr(M):
    """ Returns trace of matrix M """
    return M[0,0]+M[1,1]

# --------------------------------------------

def inverse(M):
    """ Returns the inverse of M as a matrix where all entries are type fractions.Fraction (rational) """
    a1=M[0,0].numerator
    b1=M[0,0].denominator

    a2=M[0,1].numerator
    b2=M[0,1].denominator  

    a3=M[1,0].numerator
    b3=M[1,0].denominator
    
    a4=M[1,1].numerator
    b4=M[1,1].denominator
    
    dnum = a1*a4*b2*b3-a2*a3*b1*b4 # Numerator and denominator of determinant
    ddem = b1*b2*b3*b4
    
    N = np.matrix([(Fraction(dnum*a4,ddem*b4) ,Fraction(-dnum*a2,ddem*b2)),(Fraction(-dnum*a3,ddem*b3) ,Fraction(dnum*a1,ddem*b1))])
    
    return N

# --------------------------------------------

def multiply(N,M):
    """ Returns the product NM. Assumes each entry in the matrices N, M and NM are type fractions.Fraction """
    a1=M[0,0].numerator
    b1=M[0,0].denominator

    a2=M[0,1].numerator
    b2=M[0,1].denominator  

    a3=M[1,0].numerator
    b3=M[1,0].denominator
    
    a4=M[1,1].numerator
    b4=M[1,1].denominator
    
    c1=N[0,0].numerator
    d1=N[0,0].denominator

    c2=N[0,1].numerator
    d2=N[0,1].denominator  

    c3=N[1,0].numerator
    d3=N[1,0].denominator
    
    c4=N[1,1].numerator
    d4=N[1,1].denominator
    
    R00 = Fraction(a1*d2*c1*b3 + a3*b1*c2*d1 , d1*d2*b1*b3)
    R01 = Fraction(a2*c1*d2*b4 + c2*a4*b2*d1 , b2*d1*d2*b4)
    R10 = Fraction(a1*b3*c3*d4 + a3*b1*c4*d3 , d3*d4*b1*b3)
    R11 = Fraction(a2*c3*b4*d4 + c4*a4*b2*d3 , b2*b4*d3*d4)
    
    return np.matrix( [ (R00,R01)  , (R10, R11) ] )

# --------------------------------------------

def mult(k,M):
    """
        Multiplies the matrix M by scalar k.
            Parameters:
                        k (numbers.Rational?): rational number
                        M (np.matrix): matrix with all entries of type fraction.Fraction (rational)
            Return: 
                    np.matrix : matrix k*M where all entrex are type fraction.Fraction (rational)
    """
    # TO DO: add check for k?
    a1=M[0,0].numerator
    b1=M[0,0].denominator

    a2=M[0,1].numerator
    b2=M[0,1].denominator  

    a3=M[1,0].numerator
    b3=M[1,0].denominator
    
    a4=M[1,1].numerator
    b4=M[1,1].denominator

    return np.matrix( [ (Fraction(k*a1,b1),Fraction(k*a2,b2)) , ( Fraction(k*a3,b3), Fraction(k*a4,b4))] )   # TO DO: change to np.array, apparently np.matrix may be deprecated


