#include <iostream>
#include <time.h>
#include <unistd.h>
#include <curses.h>

using namespace std;

void header(){
	cout << "|-----------------------------|" << endl;
	cout << "|    ~    Odd or Even     ~   |" << endl;
	cout << "|-----------------------------|" << endl << endl;
}

struct Dice {
  int value;
};

Dice rollDice() {
  Dice dice;
  dice.value = rand() % 6 + 1;
  return dice;
}

int main(){
	
	srand(time(NULL));
	Dice dice;
	
//	initscr();
//	printw("\n========================================\n");
//	printw("=------------| Odd or Even |-----------=\n");
//	printw("========================================\n\n");
//	printw("Tekan ENTER untuk melanjutkan...");
//	getch();
//	endwin();
	
	header();
	
	int saldo, taruhan, pilih;
	char repeat;
	
	cout << "Masukkan saldo anda = $";
	cin >> saldo;
	sleep (1);
	system ("CLS");
	
	srand(time(NULL));
	
	do {
		header();
		
		cout << "Saldo : $" << saldo << endl << endl;
		
		cout << "Masukkan taruhan : $";
		cin >> taruhan;
		
		if(saldo < taruhan){
			cout << "Taruhan anda tidak cukup." << endl;
			sleep (1);
			system ("CLS");
		}else{
			cout << "[1] Ganjil" << endl;
			cout << "[2] Genap" << endl;
			cout << "[1] / [2] : ";
			cin >> pilih;
		
			dice = rollDice();
    		cout << "\nDadu : " << dice.value << endl;
    	
    		if (dice.value % 2 == 0) {
   				if(pilih == 2){
   				 	cout << "\nSaldo anda bertambah $" << taruhan << endl;
   				 	saldo = saldo + taruhan;
					}
				else{
   					cout << "\nSaldo anda berkurang $" << taruhan << endl;
					saldo = saldo - taruhan;
				}
 	 		} 
 	 		if (dice.value % 2 != 0){
   				if(pilih == 1){
   				 	cout << "\nSaldo anda bertambah $" << taruhan << endl;
   			 		saldo = saldo + taruhan;
					}
				else{
   					cout << "\nSaldo anda berkurang $" << taruhan << endl;
					saldo = saldo - taruhan;
				}
			}
		
			cout << "Saldo : $" << saldo << endl;
		
			if (saldo == 0){
				cout << "\nSaldo anda tidak cukup.";
				sleep (2);
				repeat = 'n';
				system ("CLS");
			}
			else{
				cout << "\n\nApakah Anda ingin bermain lagi ( y / n ) : ";
				cin >> repeat;
				system ("CLS");
			}

		}
	}while(repeat!='n' );
	
	cout << "|-----------------------------|" << endl;
	cout << "|    ~  Have a Nice Day   ~   |" << endl;
	cout << "|-----------------------------|" << endl;
	
	return 0;
}
