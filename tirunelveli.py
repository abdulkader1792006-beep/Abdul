#include <iostream>
#include <string>
using namespace std;

int main() {
    int choice;

    cout << "Welcome to Tirunelveli City Guide\n";
    cout << "----------------------------------\n";
    cout << "1. About Tirunelveli\n";
    cout << "2. Famous Places\n";
    cout << "3. Famous Food\n";
    cout << "4. Exit\n";
    cout << "Enter your choice: ";
    cin >> choice;

    switch(choice) {
        case 1:
            cout << "\nTirunelveli is a historic city in Tamil Nadu.\n";
            cout << "It is known for temples, culture, and the Tamirabarani River.\n";
            break;

        case 2:
            cout << "\nFamous Places in Tirunelveli:\n";
            cout << "- Nellaiappar Temple\n";
            cout << "- Courtallam Waterfalls\n";
            cout << "- Agasthiyar Falls\n";
            cout << "- Manimuthar Dam\n";
            break;

        case 3:
            cout << "\nFamous Food:\n";
            cout << "Tirunelveli Halwa is very famous and delicious!\n";
            break;

        case 4:
            cout << "\nThank you for using Tirunelveli City Guide!\n";
            break;

        default:
            cout << "\nInvalid choice!\n";
    }

    return 0;
}
