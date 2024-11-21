#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>

#include "conveyer.h"

int main()
{
    int col_files;
    std::cout << "Input count of file needed to read: ";
    std::cin >> col_files;

    Conveyer conv(col_files);
    conv.execute();

    return 0;
}