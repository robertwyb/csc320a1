## CSC320 Winter 2018 
## Assignment 1
## (c) Kyros Kutulakos
##
## DISTRIBUTION OF THIS CODE ANY FORM (ELECTRONIC OR OTHERWISE,
## AS-IS, MODIFIED OR IN PART), WITHOUT PRIOR WRITTEN AUTHORIZATION 
## BY THE INSTRUCTOR IS STRICTLY PROHIBITED. VIOLATION OF THIS 
## POLICY WILL BE CONSIDERED AN ACT OF ACADEMIC DISHONESTY

##
## DO NOT MODIFY THIS FILE ANYWHERE EXCEPT WHERE INDICATED
##

# import basic packages
import numpy as np
import scipy.linalg as sp
import cv2 as cv

# If you wish to import any additional modules
# or define other utility functions, 
# include them here

#########################################
## PLACE YOUR CODE BETWEEN THESE LINES ##
#########################################


#########################################

#
# The Matting Class
#
# This class contains all methods required for implementing 
# triangulation matting and image compositing. Description of
# the individual methods is given below.
#
# To run triangulation matting you must create an instance
# of this class. See function run() in file run.py for an
# example of how it is called
#
class Matting:
    #
    # The class constructor
    #
    # When called, it creates a private dictionary object that acts as a container
    # for all input and all output images of the triangulation matting and compositing 
    # algorithms. These images are initialized to None and populated/accessed by 
    # calling the the readImage(), writeImage(), useTriangulationResults() methods.
    # See function run() in run.py for examples of their usage.
    #
    def __init__(self):
        self._images = { 
            'backA': None, 
            'backB': None, 
            'compA': None, 
            'compB': None, 
            'colOut': None,
            'alphaOut': None, 
            'backIn': None, 
            'colIn': None, 
            'alphaIn': None, 
            'compOut': None, 
        }

    # Return a dictionary containing the input arguments of the
    # triangulation matting algorithm, along with a brief explanation
    # and a default filename (or None)
    # This dictionary is used to create the command-line arguments
    # required by the algorithm. See the parseArguments() function
    # run.py for examples of its usage
    def mattingInput(self): 
        return {
            'backA':{'msg':'Image filename for Background A Color','default':None},
            'backB':{'msg':'Image filename for Background B Color','default':None},
            'compA':{'msg':'Image filename for Composite A Color','default':None},
            'compB':{'msg':'Image filename for Composite B Color','default':None},
        }
    # Same as above, but for the output arguments
    def mattingOutput(self): 
        return {
            'colOut':{'msg':'Image filename for Object Color','default':['color.tif']},
            'alphaOut':{'msg':'Image filename for Object Alpha','default':['alpha.tif']}
        }
    def compositingInput(self):
        return {
            'colIn':{'msg':'Image filename for Object Color','default':None},
            'alphaIn':{'msg':'Image filename for Object Alpha','default':None},
            'backIn':{'msg':'Image filename for Background Color','default':None},
        }
    def compositingOutput(self):
        return {
            'compOut':{'msg':'Image filename for Composite Color','default':['comp.tif']},
        }
    
    # Copy the output of the triangulation matting algorithm (i.e., the 
    # object Color and object Alpha images) to the images holding the input
    # to the compositing algorithm. This way we can do compositing right after
    # triangulation matting without having to save the object Color and object
    # Alpha images to disk. This routine is NOT used for partA of the assignment.
    def useTriangulationResults(self):
        if (self._images['colOut'] is not None) and (self._images['alphaOut'] is not None):
            self._images['colIn'] = self._images['colOut'].copy()
            self._images['alphaIn'] = self._images['alphaOut'].copy()

    # If you wish to create additional methods for the 
    # Matting class, include them here

    #########################################
    ## PLACE YOUR CODE BETWEEN THESE LINES ##
    #########################################

    #########################################
            
    # Use OpenCV to read an image from a file and copy its contents to the 
    # matting instance's private dictionary object. The key 
    # specifies the image variable and should be one of the
    # strings in lines 54-63. See run() in run.py for examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # leave the matting instance's dictionary entry unaffected and return
    # False, along with an error message
    def readImage(self, fileName, key):
        success = False
        msg = 'fail to read'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        self._images[key] = cv.imread(fileName)
        #if (self._images[key] is not None):
        #    success = True
        #    return success
        success = True

        #########################################
        return success, msg

    # Use OpenCV to write to a file an image that is contained in the 
    # instance's private dictionary. The key specifies the which image
    # should be written and should be one of the strings in lines 54-63. 
    # See run() in run.py for usage examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # return False, along with an error message
    def writeImage(self, fileName, key):
        success = False
        msg = 'fail to write'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        if (self._images[key] is not None):
            cv.imwrite(fileName, self._images[key])
        #    success = True
        #    return success
        success = True
        #########################################
        return success, msg

    # Method implementing the triangulation matting algorithm. The
    # method takes its inputs/outputs from the method's private dictionary 
    # ojbect. 
    def triangulationMatting(self):
        """
success, errorMessage = triangulationMatting(self)
        
        Perform triangulation matting. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """

        success = False
        msg = 'fail to mat'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        
        img_size = self._images['compA'].shape
        #for_red = np.zeros((img_size[0], img_size[1]))
        #for_blue = np.zeros((img_size[0], img_size[1]))
        #for_green = np.zeros((img_size[0], img_size[1]))
        #b1r = np.zeros
        for_c = np.zeros(img_size[:])
        alpha = np.zeros(img_size[:2])

        # get four images info
        b1 = self._images['backA']
        b2 = self._images['backB']
        c1 = self._images['compA']
        c2 = self._images['compB']
        b1r = b1g = b1b = np.zeros(img_size[:2])
        b2r = b2g = b2b = np.zeros(img_size[:2])
        c1r = c1g = c1b = np.zeros(img_size[:2])
        c2r = c2g = c2b = np.zeros(img_size[:2])


        # get matrix with selected color

        for i in range(img_size[0]):
            for j in range(img_size[1]):
                b1r[i, j] = b1[i][j][2]
                b1g[i, j] = b1[i][j][1]
                b1b[i, j] = b1[i][j][0]
                b2r[i, j] = b2[i][j][2]
                b2g[i, j] = b2[i][j][1]
                b2b[i, j] = b2[i][j][0]
                c1r[i, j] = c1[i][j][2]
                c1g[i, j] = c1[i][j][1]
                c1b[i, j] = c1[i][j][0]
                c2r[i, j] = c2[i][j][2]
                c2g[i, j] = c2[i][j][1]
                c2b[i, j] = c2[i][j][0]



        matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])

        # matrix calculation is built based on equations in 
        # http://cs.brown.edu/courses/cs129/results/final/njooma/
        for i in range(img_size[0]):
            for j in range(img_size[1]):
                c_delta = np.array([
                    [c1r[i, j] - b1r[i, j]],
                    [c1g[i, j] - b1g[i, j]],
                    [c1b[i, j] - b1b[i, j]],
                    [c2r[i, j] - b2r[i, j]],
                    [c2g[i, j] - b2g[i, j]],
                    [c2b[i, j] - b2b[i, j]]])
                bgi = np.array([
                    [b1r[i, j]],
                    [b1g[i, j]],
                    [b1b[i, j]],
                    [b2r[i, j]],
                    [b2g[i, j]],
                    [b2b[i, j]]])
                calc = np.hstack((matrix, bgi * -1))
                result = np.dot(sp.pinv(calc), c_delta)
                #result = np.clip(result, 0, 1)
                #for_red[i, j] = result[0][0]
                #for_green[i, j] = result[1][0]
                #for_blue[i, j] = result[2][0]
                #for_c[i, j] = np.array([for_red[i, j], for_green[i, j], for_blue[i, j]])
                for_c[i, j] = np.array([result[0][0], result[1][0], result[2][0]])
                alpha[i, j] = result[3]
        self._images['colOut'] = for_c
        self._images['alphaOut'] = alpha
        #if (self._images['colOut'] is not None and self._images['alphaOut'] is not None):
        #    success = True
        #    return success
        success = True     

        #########################################

        return success, msg

        
    def createComposite(self):
        """
        success, errorMessage = createComposite(self)
        
        Perform compositing. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """

        success = False
        msg = 'fail to composite'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        #img_size = self._images['backIn'].shape()
        t_alpha = self._images['alphaIn']
        t_col = self._images['colIn']
        t_comp = np.zeros(t_col.shape[:])
        
        for i in range(t_col.shape[0]):
            for j in range(t_col.shape[1]):
                colIn = t_col[i, j]
                alphaIn = t_alpha[i, j]
                backIn = self._images['backIn'][i, j]
                t_comp[i, j] = colIn + (1 - alphaIn) * backIn
        self._images['compOut'] = t_comp
        #if self._images['compOut'] is not None:
        #    success = True
        #    return success
        success = True
        #########################################

        return success, msg


