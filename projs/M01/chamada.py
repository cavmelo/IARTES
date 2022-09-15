def cada_coisa(msg="uma saida"):
    """

    :rtype: None
    """
    print(msg)
    if msg == "uma saida":
        print("usando mensagem padrão")


def main():
    cada_coisa()
    print("outra coisa")
    cada_coisa("duas ")


if __name__ == '__main__':
    main()
