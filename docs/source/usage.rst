Data Preparation
================

Spotscope has two main stages: pretraining and inference.  
For :ref:`Stage 1: Pretraining <stage-1-pretraining>`, Anndata format data needs to be prepared.  
For :ref:`Stage 2: Inference <stage-2-inference>`, there are two options: one is to use Anndata format, and the other is to perform inference directly from images.

Stage 1: Pretraining
---------------------

For pretraining, an `Anndata`_ format file needs to be prepared for each slice containing manually annotated information.  
For example, ``adata = sc.Anndata(...)``  
The Anndata format data must contain the following:

- **H&E tissue images**, ``adata.uns['spatial']``:  
  Requirements:  
  1. Each tissue slice should ideally be 10000*10000 pixels in size.  
  2. JPG format.  
  3. Save it in ``adata.uns['spatial']['test']['images']``, refer to the following code:

    .. code-block:: python
        from PIL import Image
        import numpy as np

        img_path = f"/path/to/HE_image.jpg"
        image = Image.open(img_path)
        image_array = np.array(image)

        adata_st.uns["spatial"] = {
            "test": {
                "images": {
                    "hires": image_array,
                },
                "scalefactors": {
                    "tissue_hires_scalef": 1,  
                    "spot_diameter_fullres": 150
                },
            },
        }

- **Spatial coordinates**, ``adata.obsm['spatial']``:  
  The spatial coordinates of each spot need to match the pixel points of the image.

- **Numerical annotation data**, ``adata.obsm['annotations']``:  
  This includes the annotation information for each spot, with a shape of :math:`(N, D)`, where :math:`N` is the number of spots and :math:`D` is the dimensionality of the annotation information. For example:
  
    .. code-block:: python
        array([[0.86716461, 0.04292905, 0.17157004, 0.00519644],
               [0.29841931, 0.2669554 , 0.29310532, 0.4259347 ],
               [0.30084642, 0.23525733, 0.18911946, 0.77140415],
               ...,
               [0.40642839, 0.20846453, 0.4081279 , 0.30388277],
               [0.24152377, 0.15219514, 0.28287087, 0.1691436 ],
               [0.39927267, 0.26519486, 0.20757229, 0.4316468 ]])

    .. note::
       Continuous annotation data should be normalized to the range :math:`[0, 1]`, while discrete annotation data only needs to be one-hot encoded.

- **Annotation list**, ``adata.uns['annotation_list']``:  
  A list of strings that contains the meaning of each dimension for the annotation information. For example, for a cell-type deconvolution task, it might look like:
  
    .. code-block:: python
        array(['GC', 'M/TC', 'PGC', 'OSNs'], dtype=object)

Stage 2: Inference
------------------

For the inference stage, there are two input formats:

1. As in the pretraining stage, input an Anndata class containing all information except ``adata.uns['annotations']``.  
   Reference: :ref:`1MOB_infer_celltype <notebooks/1MOB_infer_celltype.ipynb>`

2. Directly input the image and the annotation list. Spotscope will automatically detect the positions of the spots in the image and extract the coordinate information.  
   Reference: :ref:`3MOB_from_image <notebooks/3MOB_from_image.ipynb>`

Contact Information
-------------------

Please contact Jiacheng Leng (<amssljc@163.com>) if you have any problems.

.. _Anndata: https://anndata.readthedocs.io/en/latest/
