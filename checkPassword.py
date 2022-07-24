import re
def CheckPassword(s : str):
    if len(s) < 8:
        print("En az 8 karakter gerekmektedir.")
        return False
    if " " in s:
        print("Parola boşluk içeremez.")
        return False
    if not re.search("[a-z]", s):
        print("Parola en az 1 tane küçük harf içermelidir.")
        return False
    if not re.search("[A-Z]", s):
        print("Parola en az 1 tane büyük harf içermelidir.")
        return False
    if not re.findall("[0-9]", s):
        print("Parola en az 1 tane rakam içermelidir.")
        return False
    if not re.search("[@_$.#]", s):
        print("Parola en az 1 tane özel karakter içermelidir.")
        return False
    if "birklavyeden" in s:
        print("Parola isminizi içermemelidir.")
        return False
    return True
