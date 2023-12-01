import cv2

def compress_image_opencv(input_path, output_path, quality=85):
    try:
        # Read the image
        img = cv2.imread(input_path)

        # Set the JPEG compression quality (0-100)
        compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality]

        # Save the compressed image
        cv2.imwrite(output_path, img, compression_params)

        print(f"Image compressed successfully. Output saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = "img.jpg"
output_image_path = "compressed_image_opencv.jpg"
compress_image_opencv(input_image_path, output_image_path)
