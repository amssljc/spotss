Core functions
================

.. function:: infer_base(reference_spot_ebd, reference_annotations, query_img_ebd, similarity_matrix=None, num_neighbors=5, topk=5, mode="basic", annotation_type="continuous")
   :noindex:

   Execute the inference process by finding the top-k most similar embeddings in reference_spot_ebd based on query_img_ebd. Process the embeddings according to the specified mode.

   :param torch.Tensor query_img_ebd: Query image embeddings, dimension (M, D).
   :param torch.Tensor reference_spot_ebd: Reference spot embeddings, dimension (N, D).
   :param torch.Tensor reference_annotations: Reference spot annotations, dimension (N, F).
   :param torch.Tensor similarity_matrix: Spatial similarity matrix, dimension (M, M), used only in 'advanced' mode.
   :param int num_neighbors: Number of similar img_ebd to consider in low similarity situations, used only in 'advanced' mode.
   :param int topk: Number of top similar vectors to find for each query vector.
   :param str mode: 'basic' or 'advanced', specifies the processing mode.
   :param str annotation_type: 'continuous' or 'discrete', specifies the type of annotations.
   :return: A tuple containing inferred spot embeddings and annotations, dimensions (M, D) and (M, F) respectively.

.. function:: infer(adata, topk=20, lower_perc=0.1, mode="advanced", device="cuda:0", annotation_type="continuous")
   :noindex:

   Infer the annotations of spots within an AnnData object using specified inference parameters.

   :param AnnData adata: An AnnData object containing the data.
   :param int topk: Number of top matches to consider for inference.
   :param float lower_perc: Lower percentage for normalization of cell type annotation.
   :param str mode: Specifies the mode of inference ('advanced' for detailed processing).
   :param str device: Specifies the computation device, e.g., 'cuda:0'.
   :param str annotation_type: Specifies whether the annotation type is 'continuous' or 'discrete'.
   :return: Modifies the adata object with inferred spot embeddings and annotations.

.. function:: super_infer(adata, scale=2, distance_threshold=160, topk=20, lower_perc=0.1, mode="basic", annotation_type="continuous", device="cuda:0")
   :noindex:

   Perform super-resolution inference to identify annotations of spots at a higher spatial resolution.

   :param AnnData adata: An AnnData object containing the data.
   :param int scale: Scale factor for super-resolution.
   :param int distance_threshold: Distance threshold for generating super points.
   :param int topk: Number of top matches to consider for inference.
   :param float lower_perc: Lower percentage for normalization of cell type annotation.
   :param str mode: Specifies the mode of inference ('basic' for standard processing).
   :param str annotation_type: Specifies whether the annotation type is 'continuous' or 'discrete'.
   :param str device: Specifies the computation device, e.g., 'cuda:0'.
   :return: Returns a modified AnnData object at a higher resolution with inferred data.

.. function:: infer_from_image(image_path, model_path, reference_adata_paths=None, model=CLIPModel(), grid_size=112, density_threshold=0.9, mode="basic", topk=20, lower_perc=0.2, annotation_type="discrete", annotation_list=None, device='cuda:0')
   :noindex:

   Infer annotations of spots directly from an image file using a pre-trained model.

   :param str image_path: Path to the input image file.
   :param str model_path: Path to the pre-trained model.
   :param list reference_adata_paths: List of paths to reference datasets, optional.
   :param CLIPModel model: The model to use for inference.
   :param int grid_size: Grid size for processing the image.
   :param float density_threshold: Density threshold for processing spots in the image.
   :param str mode: Specifies the mode of inference ('basic' for standard processing).
   :param int topk: Number of top matches to consider for inference.
   :param float lower_perc: Lower percentage for normalization of cell type annotation.
   :param str annotation_type: Specifies whether the annotation type is 'continuous' or 'discrete'.
   :param list annotation_list: List of annotations if not using reference datasets.
   :param str device: Specifies the computation device, e.g., 'cuda:0'.
   :return: An AnnData object containing inferred spot annotations.

.. function:: image_generation(adata, pesudo_annotation, topk=10, mode='GFF', device="cuda:0")
   :noindex:

   Generate images based on pseudo annotations and model predictions.

   :param AnnData adata: An AnnData object that includes the model and reference data.
   :param ndarray pesudo_annotation: Pseudo annotations for generating images.
   :param int topk: Number of top matches to use for image generation.
   :param str mode: Generation mode, 'GFF' for guided fusion or 'mean' for averaging.
   :param str device: Specifies the computation device, e.g., 'cuda:0'.
   :return: A tensor of generated images.
