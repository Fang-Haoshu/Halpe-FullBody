## Halpe-COCO API: COCO API for [Halpe-FullBody dataset](https://github.com/Fang-Haoshu/Halpe-FullBody)
- We get this API by modifying the [COCO API](https://github.com/cocodataset/cocoapi) to adapt to the Halpe-FullBody dataset.

## Details:
- Modify the function showAnns in [PythonAPI/halpecocotools/coco.py](PythonAPI/halpecocotools/coco.py#L236) so that it can show 136 full body keypoints.
- Modify the evaluation code in [PythonAPI/halpecocotools/cocoeval.py](PythonAPI/halpecocotools/cocoeval.py) to adapt to the 136-keypoints case.

## To install:

- Run `pip install halpecocotools`.

