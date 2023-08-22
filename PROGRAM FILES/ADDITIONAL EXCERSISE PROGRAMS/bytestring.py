def main():
    
    bs= bytes([0x41, 0x42,0x43,0x44])
    print(bs)
    
    s = "sagar"
    print(s)
    
    #print(bs+s)
    
    s1 = bs.decode("utf-8")
    
    print(s+s1)
    
    bs1 = s.encode('utf-8')
    
    print(bs+bs1)
if __name__ == "__main__":
    main()