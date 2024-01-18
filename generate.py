from PIL import Image
import cv2
from pipe_Colorization import ImageColorizationPipeline


colorizer = ImageColorizationPipeline(model_path='models/pytorch_model.pt',
                                       input_size=512)

def generate(image):
    image_in = cv2.imread(image)
    image_out = colorizer.process(image_in)
    cv2.imwrite('out.jpg', image_out)
    image_in_pil = Image.fromarray(cv2.cvtColor(image_in, 
                                                cv2.COLOR_BGR2RGB))
    image_out_pil = Image.fromarray(cv2.cvtColor(image_out,
                                                  cv2.COLOR_BGR2RGB))
    return (image_in_pil, image_out_pil)
