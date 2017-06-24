def decode():
    n = int(input())
    ad_list = []
    for _ in range(n):
        al = [int(x) for x in input().split()]
        ad_list.append(al[2:])

    return n, ad_list


def convert(n, ad_list):
    ad_matrices = []
    for al in ad_list:
        tmp = [0] * n
        for i in al:
            tmp[i-1] = 1
        ad_matrices.append(tmp)

    return ad_matrices


def disp(ad_matrices):
    for al in ad_matrices:
        print(" ".join([str(x) for x in al]))

if __name__ == '__main__':

    n, ad_list = decode()
    ad_matrices = convert(n, ad_list)
    disp(ad_matrices)