# bakgrund syfte

* Förklara koden som fanns och vad den gjorde.

När jag först fick koden så var det ett 4x4 stort fält med 16 celler. Man fick välja en cell som man ville gräva genom att först skriva rad och sedan skriva kolumn. Om man grävde en säker cell så stod det "You are safe!" och man kunde fortsätta gräva. Jag tror att det bara fanns två minor och man kunde gräva samma cell om och om igen. Om man grävde en mina så stod det "Game Over!" och man kunde inte fortsätta. Om man vann genom att gräva alla rätta celler så hände ingenting.

* Vad har du lagt till för något och varför.

Jag förstorade fältet från 4x4 till 10x8 men ändrade det sedan till 10x10 för att jag råkade ofta skriva 9 i rows när det inte fanns mer än 8 rows vilket resulterade att programmet slutade att köra. Jag ändrade antalet minor från 2 till 10. Jag gjorde så att man inte kunde gräva samma mina flera gånger, när man försökte det så stod det att den redan var uppgrävd. Jag gjorde så att detn prinrade ASCI-konst av en tumme-upp när man grävde upp alla 90 celler. Tummen gjorde jag för att implementera juice och allt annat för att det skulle bli mer likt Googles minesweeper.

hur, vad, varför

# Berätta lite om hur arbetet har gått
Arbetet har gått bra, mest för att jag var kunnig inom området och att jag fick färdigskriven kod från början som jag bara utvecklade och att jag kunde be Microsoft Copilot att skriva kod åt mig och förklara det jag inte förstod.

# Vad kan du göra mer, förbättringar jmf med riktiga minesweeper
Jag kunde ha implementerat mer juice, kanske några färger eller ljudeffekter (om det ens är möjligt). Den största skillnaden från mitt Minesweeper och riktiga Minesweeper är att man inte kan markera minor med flaggor på mitt Minesweeper. En annan skillnad är att det tar längre tid att gräva en cell i min klon eftersom att man måste skriva kolumn och rad typ som ett koordinatsystem istället för att bara klicka på en cell. Jag tror att min klon har potential, men riktiga Minesweeper är definitift bättre.