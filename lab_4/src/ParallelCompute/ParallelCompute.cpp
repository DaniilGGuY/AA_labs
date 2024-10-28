#include <iostream>
#include <cstdio>

#include "curl_parse.h"
#include "vector_urls.h"
#include "one_thread.h"
#include "multi_thread.h"

#define SAVE_DIR  "data\\"
#define REFS      "..\\urls.txt"

int main()
{
    int max_refs_col, exps_col;
    std::cout << "Input max value of references\n";
    std::cin >> max_refs_col;
    std::cout << "Input counts of experiments\n";
    std::cin >> exps_col;

    std::vector<std::string> urls;
    read_urls_from_file(urls, REFS, max_refs_col);
    std::cout << "Sequential mode: " << calc_one_thread_work(urls, SAVE_DIR, exps_col) << std::endl;
    std::cout << "Parallel mode for 1 core: " << calc_multi_threads_work(urls, SAVE_DIR, 1, exps_col) << std::endl;
    std::cout << "Parallel mode for 2 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 2, exps_col) << std::endl;
    std::cout << "Parallel mode for 4 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 4, exps_col) << std::endl;
    std::cout << "Parallel mode for 8 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 8, exps_col) << std::endl;
    std::cout << "Parallel mode for 16 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 16, exps_col) << std::endl;
    std::cout << "Parallel mode for 32 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 32, exps_col) << std::endl;
    std::cout << "Parallel mode for 48 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 48, exps_col) << std::endl;
    std::cout << "Parallel mode for 64 cores: " << calc_multi_threads_work(urls, SAVE_DIR, 64, exps_col) << std::endl;

    return 0;
}