def main() -> None:
    a=[0]
    for line in open(0).read().splitlines():
        if line == '' : a.append(0) 
        if not line == '' : a[-1]+=int(line)

    print(f"first puzzle: {max(a)}")
    a.sort()
    print(f"second puzzle: {sum(a[-3:])}")
    
if __name__ == '__main__':
    main()
