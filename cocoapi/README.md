We get this API by modifying the [COCO API](https://github.com/cocodataset/cocoapi) to adapt to the Halpe-FullBody dataset.

Details:
- Finetune the function showAnns in [PythonAPI/pycocotools/coco.py](https://github.com/Fang-Haoshu/Halpe-FullBody/blob/master/cocoapi-master/PythonAPI/pycocotools/coco.py#L233) so that it can show 136 full body keypoints.
- Change the sigmas in [PythonAPI/pycocotools/cocoeval.py](https://github.com/Fang-Haoshu/Halpe-FullBody/blob/master/cocoapi-master/PythonAPI/pycocotools/cocoeval.py#L207) to adapt to the 136-keypoints case.

To install:

- For Python, run "make" under coco/PythonAPI

