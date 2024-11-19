Dataset functions
================

.. class:: CLIPDataset(adata_st, annotation=True, transform=True, patch_size=224)
    :noindex:

    Initializes a dataset object for handling spatial transcriptomics data, allowing for optional data transformations and annotations.

    :param adata_st: Either a string path to an h5ad file or an AnnData object containing the spatial transcriptomics data.
    :param annotation: A boolean flag to determine if annotations are to be loaded.
    :param transform: A boolean flag to determine if image transformations should be applied.
    :param patch_size: An integer indicating the size of the image patches to be extracted.

    This class loads high-resolution tissue images and associated spatial data from an AnnData object, applying optional image transformations such as random flips and rotations if enabled.

    .. method:: transform_img(image)
        
        Applies random transformations to an image, including horizontal flips, vertical flips, and rotations by 0, 90, 180, or 270 degrees.

        :param image: A numpy array representing the image to be transformed.
        :return: The transformed image as a numpy array.

    .. method:: __getitem__(idx)
        
        Retrieves a single data item from the dataset by index, including image data and optionally annotations.

        :param idx: An integer index specifying the data item to retrieve.
        :return: A dictionary containing transformed image data, spatial coordinates, and optionally annotations.

    .. method:: __len__()
        
        Returns the number of items in the dataset.

        :return: An integer count of the number of data items in the dataset.


.. function:: build_train_loaders(batch_size, dataset_paths, train_ratio=0.9, task='discrete', pin_memory=True, num_workers=5)
    :noindex:

    Constructs and returns DataLoader objects for both training and testing subsets of the dataset.

    :param batch_size: An integer specifying the number of items per batch.
    :param dataset_paths: A list of file paths where each path points to an h5ad file.
    :param train_ratio: A float representing the proportion of the dataset to be used for training.
    :param task: A string indicating the type of task ('discrete' or 'continuous').
    :param pin_memory: A boolean indicating whether the DataLoader should use pinned memory.
    :param num_workers: An integer specifying the number of worker processes to use.

    This function splits the dataset into training and testing portions, optionally applying weighted sampling for imbalanced datasets in discrete tasks.


.. function:: build_loaders_references(dataset_paths, num_workers=5)
    :noindex:

    Creates DataLoader for reference datasets from a list of Anndata files.

    :param dataset_paths: A list of strings, where each string is a path to an h5ad file.
    :param num_workers: An integer specifying the number of worker processes to use.
    :return: A tuple containing the DataLoader, the concatenated dataset, the size of each dataset in the list, and the annotation list.

    This function reads the annotation list from the first dataset, constructs a DataLoader for multiple datasets, and prints the construction status.


.. function:: build_loaders_querys(adata, num_workers=5)
    :noindex:

    Builds a DataLoader for querying datasets based on provided AnnData.

    :param adata: An AnnData object containing the dataset for querying.
    :param num_workers: An integer specifying the number of worker processes to use.
    :return: A tuple containing the DataLoader, the dataset, and the size of the dataset.

    This function constructs a DataLoader for the querying process and provides feedback on the loader construction.


.. function:: load_reference_datasets(adata, dataset_paths)
    :noindex:

    Loads reference datasets and updates the provided AnnData object with DataLoader and dataset information.

    :param adata: The AnnData object to update.
    :param dataset_paths: A list of file paths to h5ad files or None.

    If dataset_paths is None, it checks for existing annotations in the AnnData object, raises an assertion error if not found, and then updates the AnnData object with reference dataset information.


.. function:: load_query_datasets(adata)
    :noindex:

    Loads query datasets into the provided AnnData object.

    :param adata: The AnnData object to update.

    This function builds a DataLoader for query datasets and updates the AnnData object with the query DataLoader and dataset information.
