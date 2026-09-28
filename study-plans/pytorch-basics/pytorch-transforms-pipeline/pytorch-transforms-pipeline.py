import torch

class TransformPipeline:
    
    def __init__(self, mean: list, std: list):
        self.mean = torch.tensor(mean, dtype=torch.float32)
        self.std = torch.tensor(std, dtype=torch.float32)

    def __call__(self, image: torch.Tensor) -> torch.Tensor:
        """
        Returns a normalized float32 tensor with shape (C, H, W).
        """
        
        # input is HWC --> channel is last input
        image = image / 255

        # channel is first input now CHW
        image = torch.permute(image, (2, 0, 1))

        C,H,W = image.shape
        # normalize
        image = (image - self.mean.reshape(C,1,1)) / self.std.reshape(C,1,1)
        
        return image

        