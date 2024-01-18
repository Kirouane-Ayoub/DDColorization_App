## what is DDColor ? 




![Screenshot from 2024-01-18 15-55-58](https://github.com/Kirouane-Ayoub/DDColorization_App/assets/99510125/7907e151-e1da-4b43-b64c-f1b7fcf55eed)


DDColor is an end-to-end method for image colorization that addresses challenges such as multi-modal uncertainty, high ill-posedness, incorrect semantic colors, and low color richness. The approach proposed in DDColor involves the use of dual decoders:

Pixel Decoder: This decoder is responsible for restoring the spatial resolution of the image.

Query-Based Color Decoder: The second decoder utilizes rich visual features to refine color queries. Instead of relying on manually designed priors, this decoder leverages a query-based mechanism, which helps in avoiding hand-crafted priors.

The two decoders in DDColor work collaboratively to establish correlations between color and multi-scale semantic representations through cross-attention. This collaborative effort significantly alleviates the color bleeding effect, which is a common issue in image colorization methods.

To enhance color richness, DDColor introduces a simple yet effective colorfulness loss. This loss function aims to improve the vibrancy and diversity of colors in the colorized images.

**https://arxiv.org/pdf/2212.11613.pdf**




## Usage : 


```
git clone -b dev https://github.com/camenduru/DDColor
apt -y install -qq aria2
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/cv_ddcolor_image-colorization/resolve/main/pytorch_model.pt -d DDColor/models -o pytorch_model.pt

pip install -q timm gradio gradio_imageslider
cd DDColor
!sed -i 's/from \.version import __gitsha__, __version__/# from \.version import __gitsha__, __version__/' DDColor/basicsr/__init__.py

python app.py
```


![Screenshot from 2024-01-18 15-42-21](https://github.com/Kirouane-Ayoub/DDColorization_App/assets/99510125/e5c03cf2-9b40-4690-82c8-efcf05c6f99b)

