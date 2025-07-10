 Proiect Practică - Web Scraper cu Python și Selenium

Acesta este un proiect realizat în cadrul stagiului de practică, care folosește Python și Selenium pentru a căuta automat informații pe Google si a le salva intr-un fisier Excel.
 
  Descriere

Proiectul automatizează procesul de căutare pe Google, extrage rezultatele și le salveaza intr-un fisier Excel.
Este util pentru a colecta rapid informații despre un anumit subiect, fără a deschide manual browserul.

Tehnologii folosite

- Python 
- [Selenium](https://www.selenium.dev/)
- ChromeDriver (pentru a controla browserul Chrome)

Cum se folosește

1. Clonează repository-ul:
   
   git clone https://github.com/Prasacudaria/proiect-practica.git
   cd proiect-practica

2. Instalează dependențele (dacă nu le ai deja):
   
pip install selenium pandas openpyxl webdriver-manager

3.Asigură-te că ai ChromeDriver instalat și în PATH (sau în același folder cu scriptul).

4.Rulează scriptul:

python main.py

5. verifica fisierul " rezultate_google.xlsx"

 Observații !!
ChromeDriver trebuie să fie compatibil cu versiunea browserului Google Chrome instalat pe calculator.
Poți modifica termenii de căutare direct în cod, în funcție de ce informații vrei să colectezi.

👩‍💻 Autor
Proiect realizat de Daria Prasacu în cadrul practicii din vara anului 2025.
