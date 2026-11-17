"""Task 63 - Demonstrate how a Convolutional Neural Network works (NumPy from scratch):
convolution with edge-detection kernels, ReLU, max pooling, flatten."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def conv2d(img, k, stride=1):
    kh, kw = k.shape
    oh, ow = (img.shape[0] - kh) // stride + 1, (img.shape[1] - kw) // stride + 1
    out = np.zeros((oh, ow))
    for i in range(oh):
        for j in range(ow):
            out[i, j] = np.sum(img[i*stride:i*stride+kh, j*stride:j*stride+kw] * k)
    return out

relu = lambda x: np.maximum(0, x)
def max_pool(x, s=2):
    h, w = x.shape[0] // s, x.shape[1] // s
    return x[:h*s, :w*s].reshape(h, s, w, s).max(axis=(1, 3))

# Synthetic image: white square on black background
img = np.zeros((16, 16)); img[4:12, 4:12] = 1.0

vertical   = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
horizontal = vertical.T

fm_v = relu(conv2d(img, vertical));  fm_h = relu(conv2d(img, horizontal))
p_v, p_h = max_pool(fm_v), max_pool(fm_h)
flat = np.concatenate([p_v.ravel(), p_h.ravel()])

print("Input:", img.shape, "| Feature map:", fm_v.shape, "| After pooling:", p_v.shape)
print("Flattened vector length (input to dense layer):", flat.size)

fig, ax = plt.subplots(2, 3, figsize=(10, 6))
for a, im, t in zip(ax.ravel(), [img, fm_v, fm_h, np.zeros((1,1)), p_v, p_h],
                    ["Input", "Vertical-edge map", "Horizontal-edge map", "", "Pooled (vertical)", "Pooled (horizontal)"]):
    a.imshow(im, cmap="gray"); a.set_title(t); a.axis("off")
plt.savefig("outputs/task63_cnn_demo.png", dpi=120, bbox_inches="tight")
