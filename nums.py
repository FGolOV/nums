import random
nums= []
def find_missing_nums(nums):
    n= int(input('Введите длину и диапазон списка '))
    for indexy in range(n):
        I = random.randint(1, n)
        nums.append(I)
    nums_so_vsemi_chislami = []
    for drugie_indexy in range(1,n+1):
        nums_so_vsemi_chislami.append(drugie_indexy)
    resultat_sravnenija = [x for x in nums_so_vsemi_chislami + nums if x not in nums]
    print(nums)
    print(nums_so_vsemi_chislami)
    return(resultat_sravnenija)
print(find_missing_nums(nums))
