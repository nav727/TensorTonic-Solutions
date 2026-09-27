import torch

def gradient_accumulation(w_init, micro_batches: list, lr: float, accum_steps: int) -> tuple[torch.Tensor, torch.Tensor]:
    
    w_init = torch.as_tensor(w_init, dtype=torch.float32).clone().detach().requires_grad_(True)
    accum_grad = torch.zeros_like(w_init)
    last_grad = None

    for batch_num, (X, y) in enumerate(micro_batches):
        step = batch_num + 1

        loss = torch.square(w_init.T @ X - y)
        loss.backward()

        curr_grad = w_init.grad
        accum_grad += curr_grad
        w_init.grad.zero_()      

        if step % accum_steps == 0:
            with torch.no_grad():
                mean_grad = accum_grad / accum_steps
                w_init -= lr * mean_grad
                last_grad = mean_grad
                accum_grad = torch.zeros_like(w_init)

    return (w_init, last_grad)