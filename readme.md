# intro to machine learning with Python and scikit-learn

a session of the workshop "Open-Source Analysis in Neuroscience, Atlanta"

to set up for the tutorial, do the following:
1. Install Anaconda
 * **Please install Anaconda with the current version of Python, 3.6**
 * Windows: https://repo.continuum.io/archive/Anaconda3-4.3.0.1-Windows-x86_64.exe
 * OSX (Mac): https://repo.continuum.io/archive/Anaconda3-4.3.0-MacOSX-x86_64.pkg
 * Linux: https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
2. create a conda environment for the tutorial; to make sure my code will work on your computer
 * open a terminal and at the command line, type:
  
    `$ conda create -n intro-ml-sklearn python=3.5 scikit-learn=0.18.1 jupyter=1.0.0 matplotlib=2.0.0 seaborn=0.7.1`
 
 * when it asks you if it's okay to install required packages, say `y`
 
3. At the tutorial you will want to `activate` this environement by executing the following at the command line:
  * Windows: `> activate intro-ml-sklearn` (or whatever you named the environment)
  * Mac OS / Linux: `$ source activate intro-ml-sklearn`

----------------------------------------------------------------------

based (heavily) on the following tutorials:

https://github.com/jakevdp/sklearn_scipy2013

https://github.com/jakevdp/sklearn_pycon2015

https://github.com/amueller/scipy-2016-sklearn
