# NMA_notebook_downloader
NMA 2021 Jupyter Notebook Downloader (Local)

In zipped folder, there is Windows type (.exe) application that doesn't require to import third party libraries.

(Required) "urllist.txt" is xml file of entire NMA 2021 CN jupyter book that has been created by using xml-sitemaps.com

(Optinal) "urllist.txt" is all links for ipynb files that belong to NMA.

The required libraries are os, wget, and requests.

Because os and requests are default, you just have to install wget.

For anaconda,  

```
conda install -c anaconda wget 
```

For pip, 

```
pip install wget
```
