import argparse
import sys

#funkce v mainu
def main():
    
    #vstupní soubor a parametry
    muj_parser = argparse.ArgumentParser(description='Wordcounter')
    muj_parser.add_argument("nazev_souboru", help='nazev souboru ke cteni')
    muj_parser.add_argument("slova", help='Počítání slov', action = "store_true")
    muj_parser.add_argument("znaky", help='Počítání znaků', action = "store_true")
    muj_parser.add_argument("radky", help='Počítání řádků', action = "store_true")

    argumenty = muj_parser.parse_args()
    
    try:
        soubor = open(argumenty.nazev_souboru)
        text = soubor.read()
        
        if argumenty.slova and argumenty.znaky and argumenty.radky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: {znaky} , počet slov: {slova} , počet řádků: {radky} \n")
            file.close() #vždy soubor zavřít
            
        elif argumenty.znaky:
            znaky = len(text)
            print(f"\n{text}\nPočet znaků: {znaky}\n")
            file.close()
        
        elif argumenty.radky:
            radky = len(text.split("\n"))
            print(f"\n{text}\nPočet řádků: {radky} \n")
            file.close()
        
        elif argumenty.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet slov: {slova} \n")
            file.close()            
        
        elif argumenty.slova and argumenty.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: {znaky} , počet slov: {slova}\n")
            file.close()
        
        elif argumenty.radky and argumenty.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet slov: {slova} , počet řádků: {radky} \n")
            file.close()
        
        elif argumenty.radky and argumenty.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text}\nPočet znaků: {znaky} , počet řádků: {radky} \n")
            file.close()
        
        else:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: {znaky} , počet slov: {slova} , počet řádků: {radky} \n")
            file.close()
            
    #hlášení chyb        
    except PermissionError:
        print("Nemáte dostatečné oprávnění.")
    
    except:
        print("Jedná se o chybný soubor/název souboru.")    
        
if __name__ == '__main__':
    main()
            
            