#include <iostream>
#include <cstdio>

#include "curl_parse.h"
#include "vector_urls.h"
#include "one_thread.h"
#include "multi_thread.h"

#define SAVE_DIR  "..\\data\\"
#define REFS      "..\\urls.txt"
#define EXPS_COL  5

int main()
{
    int max_refs_col;
    std::cout << "Input max value of references\n";
    std::cin >> max_refs_col;

    std::vector<std::string> urls;
    read_urls_from_file(urls, REFS, max_refs_col);
    std::cout << "Sequential mode: " << calc_one_thread_work(urls, SAVE_DIR, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 1 core: " << calc_multi_threads_work(urls, SAVE_DIR, 1, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 2 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 2, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 4 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 4, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 8 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 8, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 16 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 16, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 32 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 32, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 48 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 48, EXPS_COL) << std::endl;
    std::cout << "Parallel mode for 64 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 64, EXPS_COL) << std::endl;

    return 0;
}