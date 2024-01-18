# Project
Programmas mērķis ir aprēķināt mēneša izdevumus, kuri tiek ņemti no maksājumu kartes vēstures. Izdevumi ir sadalīti piecās kategorijās - Brīvais laiks, Citi izdevumi, Degviela, Obligātie maksājumi, Pārtika. Katrai kategorijai ir piesaistīti atslēgas vārdi, pēc kuriem šī programa spēj kategorizēt maksājumus, bet kategorijā "Citi izdevumi" tiek iekļauti pāri palikušie maksājumi(nav piesaistīti atslēgas vārdi). 
Izvadē (terminal) tika izveidota jauna kolonna - Kategorija. Programma meklēja kolonnā "PARTNERA NOSAUKUMS" pēc atslēgfrāzēm attiecīgo kategoriju un kolonna "KATEGORIJA" to ievietoja attiecīgajai rindai. 
Pēc šī soļa izdarīšanas, programma sasummeja no kolonnas "SUMMA" attiescīgajai kategorijai naudas summu. Piemēram, Kategorijai "Brīvais laiks" kopējie izdevumi šomēnes bija 282,71 eiro, u.t.t. 
Nākošais solis bija no dizaina puses, uztaisīt tabulu ar 2 kolonnām  - kategorija un summa - virs šīs tabulas, aprēķināt kopsummu šī mēneša izdevumiem.
Kūku dieagramma - tika izveidota šī diagrama, lai labāk varētu redzēt izdevumu pārsvaru vienam pār otru. Šī diagramma parādās jaunā .png failā. 

Īsāk - programma katagorizē jūsu izdevumus ,izmantojot maksājumu kartes vēsturi, balstoties uz atslēgfrāzēm un nosaka naudas summu katrai kategorijai kopā. Un no šiem datiem tiek izveidota kūkas diagramma un tabula ar datiem. 


Bibliotēkas 
1.Pandas - efektīvāk dot iespēju strādāt ar tabulas formāta datiem, ietver funkcijas, lai ielasītu un saglabātu datus no dažādiem formātiem, kā arī veiktu datu analīzi, filtrēšanu, grupēšanu un transformāciju.. Vajadzīga šī bibliotēka, jo tika veiktas darbības ar .csv failu, kas ir tabulas veidā rakstīta. 

2.Numpy - šī bibliotēka ļauj vienkārši veikt matemātiskas darbības,  nodrošina efektīvas darbības ar masīviem un matricām.

3.Matplotlib - šī bibliotēka bija nepieciešama, lai varētu izveidot kūkas diagrammu un vizualizēt rezultātus.

4.Tabulate - šī biliotēka piedāvā iespēju veidot stilizētas tabulas no dažādu datu struktūrām, piemēram, sarakstiem vai masīviem.


Programmas izmantošana
Personīgi, šāda programma ļautu labāk sekot līdzi saviem personīgajiem tēriņiem. Dati tika ņemti no anonīmas personas, kura izmanto SEB banku. Šāda iespēja tiek piedāvāta Swedbankas lietotājiem, Swedbank lietotnē, toties citām bankām šādas iespējas nav. Tosties, katras bankas lietotājam ir iespēja piekļūt pie savas maksājumu vēstures, kas nodrošina datus šaj programai. Kā arī ir iespēja pašam izvēlēties kategorijas un atslēgas vārdus, kas var mainīt kopējos tēriņus.