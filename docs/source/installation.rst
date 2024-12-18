Installation
====================

0. Requirements
---------------

1. Anaconda or Miniconda.
2. CUDA version >= 11.8. (To install **torch >= 2.0**)
3. NVIDIA GPU available.

1. Configure Conda Environment
------------------------------

1. Create conda environment

    .. code-block:: bash
        
        conda create -n spotscope python=3.9

2. Activate conda environment

    .. code-block:: bash

        conda activate spotscope

2. Configure Python Environment
------------------------------

1. Install torch, for example:  
    
    .. note::

        Match the torch version with CUDA!!!
   
    .. code-block:: bash

        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

2. Check if `torch` installed with cuda version successfully:

    .. code-block:: bash

        python -c "import torch; print(torch.cuda.is_available()); print(torch.__version__)"

3. Setup Spotscope
------------------

- Download source code and install Spotscope locally

    .. code-block:: bash

        pip install -e .

- Or install Spotscope through pypi.

    .. code-block:: bash

        pip install spotscope
