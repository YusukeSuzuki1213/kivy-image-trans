from PIL import Image

def csv_calc(prop):
    calc1 = input_data - np.min(input_data)
    calc2 = np.max(input_data) - np.min(input_data)
    calc3 = 4095
    calc4 = calc1 / calc2
    scaled_data = calc4 * calc3
    im2 = scaled_data * prop * 0.01
    return Image.fromarray(im2)
