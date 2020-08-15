# bmptovga

Small program to convert BMP files for use in assembly, in 13h 256 colors VGA mode.

The program takes a BMP in indexed colors with VGA palette,
without RLE and color space information, created using
[this method](http://bitwelding.blogspot.com/2017/05/creating-images-for-legacy-pc-vga.html)
and outputs a .asm file containing image color bytes.
