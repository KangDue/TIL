for a in range(100):
    for b in range(100):
        print(max(a-1,b-1).bit_length())
        print(((a-1)^(b-1)).bit_length())