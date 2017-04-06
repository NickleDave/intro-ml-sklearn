# intro to machine learning with Python and scikit-learn

a session of the workshop "Open-Source Analysis in Neuroscience, Atlanta"

to set up for the tutorial, do the following:
1. Install Anaconda
 * **Please install Anaconda with the current version of Python, 3.6**
 * Windows: https://repo.continuum.io/archive/Anaconda3-4.3.0.1-Windows-x86_64.exe
 * OSX (Mac): https://repo.continuum.io/archive/Anaconda3-4.3.0-MacOSX-x86_64.pkg
 * Linux: https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
2. create a conda environment for the tutorial; to make sure my code will work on your computer
 * open an Anaconda prompt (should be in your programs menu after install) and at the command line, type:
  
    `$ conda create -n intro-ml-sklearn python=3.5 scikit-learn jupyter matplotlib seaborn`
 
 * if it asks you if it's okay to install required packages, say `y`
 
3. At the tutorial, you will want to open up the Anaconda prompt again and `activate` this environment:
  * Windows: `> activate intro-ml-sklearn` (or whatever you named the environment)
  * Mac OS / Linux: `$ source activate intro-ml-sklearn`

----------------------------------------------------------------------

based (heavily) on the following tutorials:

https://github.com/jakevdp/sklearn_scipy2013

https://github.com/jakevdp/sklearn_pycon2015

https://github.com/amueller/scipy-2016-sklearn
