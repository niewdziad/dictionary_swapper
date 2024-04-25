# dictionary_swapper
#
def dict_swap(data):
Ta linia definiuje funkcję dict_swap, która przyjmuje jedno argument - data, będące słownikiem do przetworzenia.

swapped_dict = {}
Tworzy nowy pusty słownik swapped_dict, który będzie przechowywał wynik zamiany kluczy i wartości.

for key, value in data.items():
Rozpoczyna pętlę przez wszystkie elementy (klucze i wartości) w przekazanym słowniku data.

try:
Rozpoczyna blok try-catch, który obsługuje ewentualne błędy podczas próby zamiany klucza i wartości.

swapped_dict[value] = key
Próbuje przypisać nowy klucz (value) na podstawie starej wartości (key) do słownika swapped_dict.

except TypeError:
Obsługuje błąd, który może wystąpić, jeśli wartość nie jest haszowalna.

pass
W tym przypadku po prostu pomija niemożliwą do obsługi wartość (nie dodaje jej do wynikowego słownika).

return swapped_dict
Zwraca nowy słownik swapped_dict, który zawiera zamienione klucze i wartości.

data = {"key1": 25, 100: "value100", "cadabra": "abra", (1,2): (3,4), "shmobject": object, False: None}
Tworzy przykładowy słownik data do przetestowania funkcji dict_swap.

print(dict_swap(data))
Wywołuje funkcję dict_swap na przykładowym słowniku data i wypisuje wynik na ekranie.