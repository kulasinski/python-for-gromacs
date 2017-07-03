# python-for-gromacs
Python postprocessing scripts for Gromacs xvg files

1. Make sure you have python installed by typing:
   $ python --version
   If you don't, install it with:
   (Ubuntu) $ sudo apt-get install python
   (OS X) $ brew install python
2. To install python libraries, 'pip' is the most convenient tool:
   (Ubuntu) $ sudo apt-get install pip
   (OS X) $ brew install pip
   then install libraries with:
   $ pip install [library-name]
3. The following libraries should be installed:
   numpy
   scipy
   matplotlib
4. To run a script, either type:
   $ python [script.py] [options]
   or directly
   $ ./[script.py] [options]
   which requires one time execution of
   $ chmod +x [script.py]
5. The following scripts are provided:

   xvg2csv converts a gmx energy output file (.xvg) to .csv which can be directly opened in MS Excel.
     usage:
     $ python xvg2csv.py file-name.xvg
     output:
     file-name.csv

   histogram creates a simple histogram of a data series provided in .xvg file
     usage:
     $ python histogram file-name.xvg [column, default=1] [bins, default=100]
     output:
     histogram.csv

   xvgplot plots chosen columns of an .xvg file
     usage:
     $ python xvgplot.py file-name.xvg [column_x:column_y, default=1:2]
     example:
     $ python xvgplot.py energy.xvg 1:2,1:3,2:4
