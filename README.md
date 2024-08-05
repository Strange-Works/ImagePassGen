# ImagePassGen

ImagePassGen is a C program that generates a secure password from an image file and a provided password seed. This leverages the unique characteristics of an image combined with a user-provided password to create a robust and unique password.

## Features

- Converts an image to a byte array.
- Generates a key from a provided password using SHA-256.
- Combines the image data with the generated key and hashes the result to create a final password.

## Prerequisites

- OpenSSL
- libpng

Install the required libraries on a Debian-based system:
```sh
sudo apt-get install libssl-dev libpng-dev
