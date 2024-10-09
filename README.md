# Potatoes Diseases Detection using YOLOv8 (Pytorch)

There's 4 classes in this trial

- Black Scurf

<img src="/test/images/28_jpg.rf.ba6b2e5783fadf44f272f38660fd1e9b.jpg" alt="bs" width="300"/>

- Blackleg

<img src="/test/images/13_jpg.rf.069749f199163ad6a5a90eec5c58153a.jpg" alt="blackleg" width="300"/>

- Healthy

<img src="/test/images/23_jpg.rf.53ad2938590e2b1e86ef5a666fcceb94.jpg" alt="healthy" width="300"/>

- Pink Rot

<img src="/test/images/23_jpg.rf.abb6cb90fd681a0617caa682b113b1f1.jpg" alt="pr" width="300"/>


## Model Evaluate

![result](/runs/detect/train2/results.png)

![test](/runs/detect/predict/23_jpg.rf.abb6cb90fd681a0617caa682b113b1f1.jpg)

## HuggingFace

I have been deploy this model in [HuggingFace](https://huggingface.co/spaces/AndikaRT421/petani-potatoes-OD). I apologize for only providing image input


## Reference

**DATASET =>** [Kaggle](https://www.kaggle.com/datasets/mukaffimoin/potato-diseases-datasets)

```
@INPROCEEDINGS{10099162,
  author={Faria, Fatema Tuj Johora and Bin Moin, Mukaffi and Al Wase, Ahmed and Sani, Md. Rabius and Hasib, Khan Md and Alam, Mohammad Shafiul},
  booktitle={2023 IEEE 13th Annual Computing and Communication Workshop and Conference (CCWC)}, 
  title={Classification of Potato Disease with Digital Image Processing Technique: A Hybrid Deep Learning Framework}, 
  year={2023},
  volume={},
  number={},
  pages={0820-0826},
  doi={10.1109/CCWC57344.2023.10099162}}
```