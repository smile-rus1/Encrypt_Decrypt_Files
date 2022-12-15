import pyAesCrypt
import os


def encrypt(file, password, type):
    try:
        # pyAesCrypt.encryptFile(str(file)+"."+ str(type), str(file) + ".aes", password)
        pyAesCrypt.encryptFile(str(file) + str(type), str(file) + ".aes", password)
        with open("password.txt", "w") as pas: pas.write(f"Ваш пароль (чтобы не забыть) {password}")
        print(f"Файл {str(os.path.splitext(file)[0])} зашифрован")
        os.remove(file + str(type))

    except:
        print("Не правильно введены данные")


def decrypt(file, password):
    try:
        pyAesCrypt.decryptFile(str(file) + ".aes", str(os.path.splitext(file)[0]), password)
        print(f"Файл {str(os.path.splitext(file)[0])} расшифрован")
        os.remove(file + ".aes")
        if os.path.exists("password.txt"):
            os.remove("password.txt")

    except:
        print("Не правильно введены данные")


def main():
    choice = input("Выберите что делать?\n(1)Шифровать\n(2)Расшифровать" +"\n")

    if choice == "1":
        file = input("Введите файл который хотите зашифровать" + "\n")
        password = input("Введите пароль для шифровки" + "\n")
        type_format = ""

        choice_format = input("Введите какой формат файла зашифровать\n(1)txt\n(2)docx" + "\n")

        match choice_format:
            case "1":
                type_format = ".txt"
            case "2":
                type_format = ".docx"

        encrypt(file, password,type_format)

    elif choice == "2":

        file = input("Введите файл который хотите расшифровать" + "\n")
        password = input("Введите пароль для шифровки" + "\n")

        decrypt(file, password)

if __name__ == '__main__':
    main()
    input("Enter for continue ...")