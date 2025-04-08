def main():

    N = int(input('Enter the number N: '))
    result = []

    result = [2**i for i in range(N+1)]
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
