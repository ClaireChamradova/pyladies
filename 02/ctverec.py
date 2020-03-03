strana = float (int (input ('Zdej stranu čtverce:')))
#float - změna na desetinná čísla, int - změna textu na číslo, input - interakce s uživatelem

cislo_je_ok = strana > 0

obvod = strana* 4
obsah = strana ** 2

# if - pokud, elif - jinak pokud, else - jinak
if cislo_je_ok:
    print ('Obvod čvterce se stranou', strana, 'cm je', obvod, 'cm.')
    print ('Obsah čtverce se stranou', strana, 'cm je', obsah, 'cm2.')
else:
    print ('Strana musí být kaldná!')

print ('Díky za použití')
