bin2go
======

Converts a file into a byte array to embed within a Go binary. For example, bundle
a TrueType font into the binary for a go-sdl2 application. Similar to bin2h for C
applications.

## Usage

```bash
# run with defaults
python bin2go.py myfile.txt

# specify maximum line length (each line won't exceed this number of chars)
python bin2go.py -width 100 myfile.txt
```

## Example

Suppose you save the following to a text file named loremipsum.txt:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

Running bin2go will yield the following:

```go
var myBytesArray []byte = []byte{
    76, 111, 114, 101, 109, 32, 105, 112, 115, 117, 109, 32, 100, 111, 108, 111, 114, 32, 115, 105, 116, 32, 97, 109, 
    101, 116, 44, 32, 99, 111, 110, 115, 101, 99, 116, 101, 116, 117, 114, 32, 97, 100, 105, 112, 105, 115, 99, 105, 
    110, 103, 32, 101, 108, 105, 116, 44, 32, 115, 101, 100, 32, 100, 111, 32, 101, 105, 117, 115, 109, 111, 100, 32, 
    116, 101, 109, 112, 111, 114, 32, 105, 110, 99, 105, 100, 105, 100, 117, 110, 116, 32, 117, 116, 32, 108, 97, 98, 
    111, 114, 101, 32, 101, 116, 32, 100, 111, 108, 111, 114, 101, 32, 109, 97, 103, 110, 97, 32, 97, 108, 105, 113, 
    117, 97, 46, 32, 85, 116, 32, 101, 110, 105, 109, 32, 97, 100, 32, 109, 105, 110, 105, 109, 32, 118, 101, 110, 105, 
    97, 109, 44, 32, 113, 117, 105, 115, 32, 110, 111, 115, 116, 114, 117, 100, 32, 101, 120, 101, 114, 99, 105, 116, 
    97, 116, 105, 111, 110, 32, 117, 108, 108, 97, 109, 99, 111, 32, 108, 97, 98, 111, 114, 105, 115, 32, 110, 105, 115, 
    105, 32, 117, 116, 32, 97, 108, 105, 113, 117, 105, 112, 32, 101, 120, 32, 101, 97, 32, 99, 111, 109, 109, 111, 100, 
    111, 32, 99, 111, 110, 115, 101, 113, 117, 97, 116, 46, 32, 68, 117, 105, 115, 32, 97, 117, 116, 101, 32, 105, 114, 
    117, 114, 101, 32, 100, 111, 108, 111, 114, 32, 105, 110, 32, 114, 101, 112, 114, 101, 104, 101, 110, 100, 101, 114, 
    105, 116, 32, 105, 110, 32, 118, 111, 108, 117, 112, 116, 97, 116, 101, 32, 118, 101, 108, 105, 116, 32, 101, 115, 
    115, 101, 32, 99, 105, 108, 108, 117, 109, 32, 100, 111, 108, 111, 114, 101, 32, 101, 117, 32, 102, 117, 103, 105, 
    97, 116, 32, 110, 117, 108, 108, 97, 32, 112, 97, 114, 105, 97, 116, 117, 114, 46, 32, 69, 120, 99, 101, 112, 116, 
    101, 117, 114, 32, 115, 105, 110, 116, 32, 111, 99, 99, 97, 101, 99, 97, 116, 32, 99, 117, 112, 105, 100, 97, 116, 
    97, 116, 32, 110, 111, 110, 32, 112, 114, 111, 105, 100, 101, 110, 116, 44, 32, 115, 117, 110, 116, 32, 105, 110, 
    32, 99, 117, 108, 112, 97, 32, 113, 117, 105, 32, 111, 102, 102, 105, 99, 105, 97, 32, 100, 101, 115, 101, 114, 117, 
    110, 116, 32, 109, 111, 108, 108, 105, 116, 32, 97, 110, 105, 109, 32, 105, 100, 32, 101, 115, 116, 32, 108, 97, 98, 
    111, 114, 117, 109, 46, 
}
```
