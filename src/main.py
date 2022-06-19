
import torch

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from typing import List

import hydra
from omegaconf import DictConfig

@hydra.main(config_path='../configs/', config_name='main.yaml')
def main(config: DictConfig):

    orig_img = Image.open('/home/didi/Repository/Augmentation-Hydra/src/astronaut.jpg')

    # Init lightning callbacks
    augmentation: List[torch.nn.Module] = []
    if "augmentation" in config:
        for _, aug_conf in config.augmentation.items():
            if "_target_" in aug_conf:
                augmentation.append(hydra.utils.instantiate(aug_conf))

    plot([aug(orig_img) for aug in augmentation])

def plot(imgs, with_orig=True, row_title=None, **imshow_kwargs):
    if not isinstance(imgs[0], list):
        # Make a 2d grid even if there's just 1 row
        imgs = [imgs]

    orig_img = Image.open('/home/didi/Repository/Augmentation-Hydra/src/astronaut.jpg')

    num_rows = len(imgs)
    num_cols = len(imgs[0]) + with_orig
    fig, axs = plt.subplots(nrows=num_rows, ncols=num_cols, squeeze=False)
    for row_idx, row in enumerate(imgs):
        row = [orig_img] + row if with_orig else row
        for col_idx, img in enumerate(row):
            ax = axs[row_idx, col_idx]
            ax.imshow(np.asarray(img), **imshow_kwargs)
            ax.set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

    if with_orig:
        axs[0, 0].set(title='Original image')
        axs[0, 0].title.set_size(8)
    if row_title is not None:
        for row_idx in range(num_rows):
            axs[row_idx, 0].set(ylabel=row_title[row_idx])

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':

    plt.rcParams["savefig.bbox"] = 'tight'
    torch.manual_seed(0)

    main()

    # augs = transforms.Compose([
    #     transforms.Resize(50)
    # ])

    # plot([augs(orig_img)])