# Installing and firing up Jupyter

* install Python and Jupyter by installing Anaconda from 
[here](https://www.anaconda.com/download/#macos)

* create a conda environment using Python 2: 
```
conda create -n lab-meeting python=2 ipython-notebook --yes
source activate lab-meeting
```

* start the Jupyter notebook server using  `jupyter notebook`

* close a jupyter notebook by pressing `ctrl-c` twice at the command prompt

* deactivate conda environment via `source deactivate`
 
# Render notebook as a live presentation

* install RISE via `conda install -c damianavila82 rise`

* New button to toggle slideshow appears in notebook toolbar

* `View -> Cell Toolbar -> Slideshow` allows one to choose how each cell is displayed in the slideshow 

References: 
https://github.com/damianavila/RISE
 https://damianavila.github.io/RISE/
