## instalation using pip:

pip install git+https://github.com/kesmarag/ml-utils.git

## usage
```python
import numpy as np
from kesmarag.ml.utils import Dataset

data = np.random.rand(1000, 20000, 10)
dataset = DataSet(data)
print(dataset.get_batch(5, 1000).shape)

# Good luck
```