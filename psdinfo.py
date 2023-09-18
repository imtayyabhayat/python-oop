from psd_tools import PSDImage
import math

def calculate_rotation(rectangle, parent):
    x1, y1, x2, y2 = rectangle.bbox
    parent_width, parent_height = (560, 933)
    # Calculate center coordinates of the parent box
    Cx = parent_width / 2
    Cy = parent_height / 2

    # Calculate center coordinates of the inner box
    Ix = (x1 + x2) / 2
    Iy = (y1 + y2) / 2

    # Calculate the difference in coordinates
    dx = Ix - Cx
    dy = Iy - Cy

    # Calculate the rotation angle in degrees
    angle_degrees = math.degrees(math.atan2(dy, dx))
    
    return angle_degrees

def extract_mask_info(psd_file_path):
    psd = PSDImage.open(psd_file_path)
    # psd.composite().save("test.png")
    for layers in psd:
        # print(layers)
        if layers.kind == "pixel":
            print(layers.size, "-->", layers.kind)
        if layers.kind == "shape" and layers.has_origination: 
            # x, y = layers.offset
            # w, h = layers.size
            # print(x, y, w, h)
            # x,y,r,b = layers.origination
            # print(layers.origination)
            for shape in layers.origination:
                # print(shape)
                x1, y1, x2, y2 = shape.bbox
                # w, h = round((x2 - x1), 2), round((y2 - y1), 2)
                w, h = layers.size
                angle = calculate_rotation(shape, layers)
                print(round(x1, 2), round(y1, 2), w, h, shape)
                # x = shape[0]
                # y = shape[1]
            # print(layers.vector_mask, "-->", layers.kind)
        # if layers.kind == "mask":
        #     print(layers.vector_mask, "-->", layers.kind)
        # if layers.kind == "text":
        #     print(layers.vector_mask, "-->", layers.kind)
    return psd

if __name__ == "__main__":
    psd_file_path = "test.psd"
    masks_info = extract_mask_info(psd_file_path)
    # print(masks_info.)
