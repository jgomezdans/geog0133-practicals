<p><img src="https://github.com/profLewis/Geog2021_Coursework/blob/master/images/ucl_logo.png?raw=true" align="left" \><img src="https://www.nceo.ac.uk/wp-content/themes/nceo/assets/images/logos/img_logo_purple.svg" align="right" /></p>

# GEOG0133 Terrestrial Carbon: modelling and monitoring
### J Gómez-Dans & P Lewis

You can run the practicals directly online, thanks to the Binder infrastructure. Here's a link to the whole repository, and individual practicals will be linked below.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgomezdans/geog0133-practicals/master)

## Practical 1: A simple Earth System Model
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgomezdans/geog0133-practicals/master?filepath=01-Simple_Earth_System_Model.ipynb)


This exercise aims to show a very simple energy balance model of the Earth system.


## Practical 2: Per Capita Carbon emissions
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgomezdans/geog0133-practicals/master?filepath=02-Emissions_Exercise.ipynb)

A simple exercise to understand carbon emissions. Includes fitting some very simple models.

## Practical 3: Photosynthesis modelling
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgomezdans/geog0133-practicals/master?filepath=03-Photosynthesis_Modelling_Practical.ipynb)
A practical where the Farquhar approach to photosynthesis in vegetation is used to explore how vegetation is modelled in typical dynamic global vegetation models (DGVMs). The practical allows you to understand (some of) the limits to photosynthetic activity in vegetation, as well as explore the role of plant functional types (PFTs) in controlling photosynthesis. The final aim is to think how this basic leaf-level model can form the basis of a vegetation carbon model.

## Practical 4: Phenology 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgomezdans/geog0133-practicals/master?filepath=04-Phenology_Modelling_Practical.ipynb)
Phenology is the study of recurrent natural phenomena. In this practical, you will try to develop models for vegetation phenology based on observations of plant "greenness" derived from satellite data, as well as abiotic controls (mostly temperature!).


### Running on your own computer

If you want run this on your own computer, you can do that easily. Follow these steps:

1. First, download or clone the entire repository. 
    a. You can download everything as a zip file, and uncompress it,
    b. ... Or you can do `git clone https://github.com/jgomezdans/geog0133-practicals` if you have git installed
2. Make sure you have Anaconda Python installed, and in the folder with the practicals issue the following command:

    ```
    conda env create -f environment.yml
    ```
3. The previous command can take a while to run, and needs the internet to download stuff.
4. You can then (hopefully) just run `jupyter notebook` on that folder
