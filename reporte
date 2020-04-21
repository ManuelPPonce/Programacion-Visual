#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <direct.h>
using namespace std;

int menu();

string crear_directorio();


int main() {
    //////////////////////////
    int Id;

    string R_ID;
    string Ajustado [1613];
    string DEPP [1613];
    string Sede [1613];
    string Nivel[1613];
    string Nombre[1613];
    string Estatus[1613];
    string Eca[1613];
    string Beca[1613];
    string Programa[1613];
    string Cargos[1613];
    string Pagado[1613];
    string Saldo[1613];
    string Saldov[1613];
    string NCV[1613];
    string id[1613];
    //////////////////////////
    int i = 0;
    int j = 0;
    int cont=0;
    //////////////////////////
    ifstream archivo;
    ofstream pagos_vencidos;
    ofstream pagos_vencidos1;
    ofstream pagos_vencidos2;
    ofstream pagos_vencidos3;
    string ruta_absoluta;
    string carpeta;
    string ss;
    string linea;
    string resultado;
    string texto;
    string arhivodeldia;
    char oldname [] = "811.txt" ;


    /*while(!archivo.eof()){//mientras no sea el final del archivo esto se puede debido a la funcion eof
        getline(archivo,texto);
        cout << texto<<endl;
    }*/
    int op;

    cout << "Seccione el archivo del dia: " ; cin >> arhivodeldia;

    archivo.open (arhivodeldia.c_str() ,ios::in);
    if(archivo.fail()){
        cout <<"No se pudo abrir el archivo";
        exit(1);
    }


    while(getline(archivo, linea)) {
        stringstream ss(linea);
        getline(ss, id[i], ',');
        Id = atoi(id[i].c_str());
        getline(ss, Nombre[i], ',');
        getline(ss, Sede[i], ',');
        getline(ss, Programa[i], ',');
        getline(ss, Nivel[i], ',');
        getline(ss, Estatus[i], ',');
        getline(ss, Beca[i], ',');
        getline(ss, Cargos[i], ',');
        getline(ss, Eca[i], ',');
        getline(ss, DEPP[i], ',');
        getline(ss, Ajustado[i], ',');
        getline(ss, Pagado[i], ',');
        getline(ss, Saldo[i], ',');
        getline(ss, Saldov[i], ',');
        getline(ss, NCV[i], ',');
        i++;
    }


        /////////////////////////////
    int salir;
    op = menu();

    while(salir != 0){
    switch (op){
        case 1:

            cout << " **REPORTE POR ID** \n";
            cout << " Ingresa el ID : "; cin >> R_ID;

            pagos_vencidos.open (R_ID.c_str(),ios::out);

            for(i = 0 ; i <= 1613 ; i++){

                if(R_ID.compare(id[i]) == 0  ){
                    pagos_vencidos <<" ID : " << id[i] << endl ;
                    pagos_vencidos <<" Nombre : " << Nombre[i] << endl;
                    pagos_vencidos <<" Programa : " << Programa[i] << endl;
                    pagos_vencidos <<" Cargos : " << Cargos[i] << endl;
                    pagos_vencidos <<" Pagado : " << Pagado[i] << endl;
                    pagos_vencidos <<" Saldo : " << Saldo[i] << endl;
                    pagos_vencidos <<" Saldo vencido : " << Saldov[i] << endl;
                    pagos_vencidos << "Numero de pagos vencidos : " << NCV[i] << endl;
                    cout << " ID : " << id[i] << endl ;
                    cout <<" Nombre : " << Nombre[i] << endl;
                    cout <<" Programa : " << Programa[i] << endl;
                    cout <<" Cargos : " << Cargos[i] << endl;
                    cout <<" Pagado : " << Pagado[i] << endl;
                    cout <<" Saldo : " << Saldo[i] << endl;
                    cout <<" Saldo vencido : " << Saldov[i] << endl;
                    cout << "Numero de pagos vencidos : " << NCV[i] << endl;

                }
                resultado = R_ID + ".txt";
                archivo.open (R_ID.c_str(), ios::in);
                while(!archivo.eof()){//mientras no sea el final del archivo esto se puede debido a la funcion eof
                    getline(archivo,texto);
                    cout << texto <<endl;
                }

            }
            pagos_vencidos.close();
            cout << endl;
            cout << endl;
            cout << " |-----------------------------------------------------------------------------------------------|\n";
            cout << " | 1) Volver a intentar por id                                                                   | \n";
            cout << " | 2) Reporte por Programa:                                                                      |\n";
            cout << " | 3) Reporte por pagos vencidos                                                                 |\n";
            cout << " | 4) Reporte por Generacion de archivo de texto para pegar en correo o mensaje de texto         |\n";
            cout << " | 5) Salir                                                                                      |\n ";
            cout << "|-----------------------------------------------------------------------------------------------|\n";
            cout << " Inserte la opcion deseada :    " ;
            cin >> op;

            break;
        case 2:
            cout << " **REPORTE POR PROGRAMA** \n";
            cout << " Ingresa el Programa : "; cin >> R_ID;
            pagos_vencidos1.open (R_ID.c_str(),ios::out);
            for(i = 0 ; i <= 1613 ; i++){
                if(R_ID.compare(Programa[i]) == 0  ){

                    pagos_vencidos1 << " ID : " << id[i] << endl ;
                    pagos_vencidos1 <<" Nombre : " << Nombre[i] << endl;
                    pagos_vencidos1 <<" Programa : " << Programa[i] << endl;
                    pagos_vencidos1 <<" Cargos : " << Cargos[i] << endl;
                    pagos_vencidos1 <<" Pagado : " << Pagado[i] << endl;
                    pagos_vencidos1 <<" Saldo : " << Saldo[i] << endl;
                    pagos_vencidos1 <<" Saldo vencido : " << Saldov[i] << endl;
                    pagos_vencidos1 << "Numero de pagos vencidos : " << NCV[i] << endl;
                    cout << " ID : " << id[i] << endl ;
                    cout <<" Nombre : " << Nombre[i] << endl;
                    cout <<" Programa : " << Programa[i] << endl;
                    cout <<" Cargos : " << Cargos[i] << endl;
                    cout <<" Pagado : " << Pagado[i] << endl;
                    cout <<" Saldo : " << Saldo[i] << endl;
                    cout <<" Saldo vencido : " << Saldov[i] << endl;
                    cout << "Numero de pagos vencidos : " << NCV[i] << endl;



                }
                }
            cout << " |-----------------------------------------------------------------------------------------------|\n";
            cout << " | 1) Volver a intentar por id                                                                   | \n";
            cout << " | 2) Reporte por Programa:                                                                      |\n";
            cout << " | 3) Reporte por pagos vencidos                                                                 |\n";
            cout << " | 4) Reporte por Generacion de archivo de texto para pegar en correo o mensaje de texto         |\n";
            cout << " | 5) Salir                                                                                      |\n ";
            cout << "|-----------------------------------------------------------------------------------------------|\n";
            cout << " Inserte la opcion deseada :    " ;
            cin >> op;
            break;
        case 3:

            cout << " **REPORTE POR PAGOS VENCIDOS* \n";
             R_ID = '0';
            pagos_vencidos2.open (oldname ,ios::out);

            for(i = 1 ; i <= 1612 ; i++){
                if(R_ID.compare(NCV[i]) != 0 ){
                    pagos_vencidos2 <<" ID : " << id[i] << endl ;
                    pagos_vencidos2 <<" Nombre : " << Nombre[i] << endl;
                    pagos_vencidos2 <<" Programa : " << Programa[i] << endl;
                    pagos_vencidos2 <<" Cargos : " << Cargos[i] << endl;
                    pagos_vencidos2 <<" Pagado : " << Pagado[i] << endl;
                    pagos_vencidos2 <<" Saldo : " << Saldo[i] << endl;
                    pagos_vencidos2 <<" Saldo vencido : " << Saldov[i] << endl;
                    pagos_vencidos2 << "Numero de pagos vencidos : " << NCV[i] << endl;
                    cout << " ID : " << id[i] << endl ;
                    cout <<" Nombre : " << Nombre[i] << endl;
                    cout <<" Programa : " << Programa[i] << endl;
                    cout <<" Cargos : " << Cargos[i] << endl;
                    cout <<" Pagado : " << Pagado[i] << endl;
                    cout <<" Saldo : " << Saldo[i] << endl;
                    cout <<" Saldo vencido : " << Saldov[i] << endl;
                    cout << "Numero de pagos vencidos : " << NCV[i] << endl;
                    cont++;
                }


            }

            cout << " |-----------------------------------------------------------------------------------------------|\n";
            cout << " | 1) Volver a intentar por id                                                                   | \n";
            cout << " | 2) Reporte por Programa:                                                                      |\n";
            cout << " | 3) Reporte por pagos vencidos                                                                 |\n";
            cout << " | 4) Reporte por Generacion de archivo de texto para pegar en correo o mensaje de texto         |\n";
            cout << " | 5) Salir                                                                                      |\n ";
            cout << "|-----------------------------------------------------------------------------------------------|\n";
            cout << " Inserte la opcion deseada :    " ;
            cin >> op;
            break;
        case 4:

            carpeta = crear_directorio();

            for(i = 1 ; i <= 1612 ; i++){
                pagos_vencidos3.open (id[i].c_str() ,ios::out);
                if(R_ID.compare(NCV[i]) != 0 ){
                    ruta_absoluta = carpeta+"\\"+id[i]+".txt";
                    cout <<ruta_absoluta;


                    cout <<" ID : " << id[i] << endl ;
                    cout <<" Nombre : " << Nombre[i] << endl;
                    cout <<" Programa : " << Programa[i] << endl;
                    cout <<" Cargos : " << Cargos[i] << endl;
                    cout <<" Pagado : " << Pagado[i] << endl;
                    cout <<" Saldo : " << Saldo[i] << endl;
                    cout <<" Saldo vencido : " << Saldov[i] << endl;
                    cout << "Numero de pagos vencidos : " << NCV[i] << endl;

                }

            }

            cout << " |-----------------------------------------------------------------------------------------------|\n";
            cout << " | 1) Volver a intentar por id                                                                   | \n";
            cout << " | 2) Reporte por Programa:                                                                      |\n";
            cout << " | 3) Reporte por pagos vencidos                                                                 |\n";
            cout << " | 4) Reporte por Generacion de archivo de texto para pegar en correo o mensaje de texto         |\n";
            cout << " | 5) Salir                                                                                      |\n ";
            cout << "|-----------------------------------------------------------------------------------------------|\n";
            cout << " Inserte la opcion deseada :    " ;
            cin >> op;
            break;
        case 5 :
            salir = 0;
            break;

    }
    }




    return 0;
}

int menu(){
    int op;
    system("cls");
    cout << " | ******************************************MENU************************************************|\n";
    cout << " |-----------------------------------------------------------------------------------------------|\n";
    cout << " | 1) Reporte por id                                                                   | \n";
    cout << " | 2) Reporte por Programa:                                                                      |\n";
    cout << " | 3) Reporte por pagos vencidos                                                                 |\n";
    cout << " | 4) Reporte por Generacion de archivo de texto para pegar en correo o mensaje de texto         |\n";
    cout << " | 5) Salir                                                                                      |\n ";
    cout << "|-----------------------------------------------------------------------------------------------|\n";
    cout << " Inserte la opcion deseada :    " ;
    cin >> op;

    return op;

}

string crear_directorio(){


    auto t = time(nullptr);
    auto tm = *localtime(&t);

    ostringstream oss;
    oss << put_time(&tm, "%d-%m-%Y ");
    auto str = oss.str();


    string ruta_abs =  str;
    string retorno;

    if (mkdir(ruta_abs.c_str()) == 0 )
    {
        cout << "Carpeta creada correctamente \n";
    }
    else {
        cout << "Ha ocurrido un error al crear la carpeta "<< endl;;
        crear_directorio();
    }


    return  ruta_abs;

}



