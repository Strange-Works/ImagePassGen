from PIL import Image
import hashlib
import io

def image_to_byte_array(image_path):
    """
    Convert an image to a byte array.
    """
    with Image.open(image_path) as image:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format)
        return img_byte_arr.getvalue()

def generate_key(password):
    """
    Generate a SHA-256 hash of the password.
    """
    return hashlib.sha256(password.encode()).digest()

def generate_password(image_path, password):
    """
    Generate a password by combining image data and a password seed.
    """
    # Convert image to byte array
    image_data = image_to_byte_array(image_path)
    
    # Generate key from password
    key = generate_key(password)
    
    # Combine image data and key
    combined = image_data + key
    
    # Generate the final password by hashing the combined data
    password_hash = hashlib.sha256(combined).hexdigest()
    
    return password_hash

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate a secure password from an image and a password seed.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("password_seed", help="Password seed")

    args = parser.parse_args()

    generated_password = generate_password(args.image_path, args.password_seed)
    
    print(f"Generated Password: {generated_password}")
