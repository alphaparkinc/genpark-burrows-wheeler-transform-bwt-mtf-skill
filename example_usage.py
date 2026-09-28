from client import BWTCoder

def main():
    text = "mississippi"
    bwt = BWTCoder.bwt_transform(text)
    print("BWT Transformed:", repr(bwt))
    recovered = BWTCoder.bwt_inverse(bwt)
    print("BWT Inverted:", recovered)
    assert recovered == text

if __name__ == "__main__":
    main()
