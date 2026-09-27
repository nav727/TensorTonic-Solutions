import torch


def gradient_accumulation(w_init: torch.Tensor, micro_batches: list, lr: float, accum_steps: int) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Returns (final_weights, last_mean_gradient) as float32 tensors.
    """
    
    w_init = w_init.requires_grad_(True)
    accum_grad = torch.zeros(w_init.shape)
    last_grad = torch.zeros(w_init.shape)
    
    for batch_num, data in enumerate(micro_batches):

        X, y = data
        
        loss = torch.square(w_init.T @ X - y)  
        loss.backward()

        curr_grad = w_init.grad
        accum_grad += curr_grad
        w_init.grad.zero_()
        
        if (batch_num + 1) % accum_steps == 0:

            # update weights
            with torch.no_grad():
                
                mean_grad = accum_grad / accum_steps
                w_init -= lr * mean_grad
                last_grad = mean_grad
                accum_grad.zero_()

    return (w_init, last_grad)
