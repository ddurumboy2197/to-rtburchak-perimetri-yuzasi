def tortburchak_perimetri_uzunliklar(a, b, c, d):
    return a + b + c + d

def tortburchak_yuzasi(a, b, c, d):
    s = tortburchak_perimetri_uzunliklar(a, b, c, d) / 2
    return (s*(s-a)*(s-b)*(s-c)*(s-d)) ** 0.5

# Misol uchun ma'lumotlarni kiritish
a = 5
b = 6
c = 7
d = 8

perimetri = tortburchak_perimetri_uzunliklar(a, b, c, d)
yuzasi = tortburchak_yuzasi(a, b, c, d)

print(f"To'rtburchakning perimetri: {perimetri}")
print(f"To'rtburchakning yuzasi: {yuzasi}")
