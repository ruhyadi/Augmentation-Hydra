# Augmentation with Hydra

Hydra gives you the power to configure augmentation without changing code in the python file (`main.py`). Instead, you can change augmentation parameters in `configs/augmentation/transforms.yaml`, or change it within a terminal. Another power of Hydra is an experiment. You can make your experiment augmentation parameters in `configs/experiment/your_exp.yaml`. 

Change augmentation with terminal:
```py
python src/main.py \
    augmentation.resize.size=150 \
    augmentation.random_crop.size=125 \
    augmentation.random_perspective.distortion_scale=0.35
```

Change augmentation with an experiment:
```py
python src/main.py experiment=your_exp
```

## Acknowledgment

- Awesome Hydra Template [ashleve/lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)

