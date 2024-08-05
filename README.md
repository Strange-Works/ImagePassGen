# ImagePassGen

ImagePassGen is a Python program that generates a secure password from an image file and a provided password seed. This leverages the unique characteristics of an image combined with a user-provided password to create a robust and unique password.

## Features

- Converts an image to a byte array.
- Generates a key from a provided password using SHA-256.
- Combines the image data with the generated key and hashes the result to create a final password.

## Prerequisites

- Python 3.x
- Pillow library

Install the required library:

```sh
pip install pillow
```

## Building and Running

1. Clone the repository or download the 'IMG2PASS.py' file.
2. Compile the code:

```sh
python IMG2PASS.py your_initial_password
```

3. Run the program:

```sh
./IMG2PASS path_to_your_image.png your_initial_password
```

4. Replace path_to_your_image.png with the path to your PNG image file and your_initial_password with your password seed.

Example

```sh
./IMG2PASS images/example.png mypassword
```

## Contact

Oliver Strange - [oliver@strangedesign.co.uk](mailto:oliver@strangedesign.co.uk)
