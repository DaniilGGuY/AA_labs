#ifndef MULTI_THREAD_H__
#define MULTI_THREAD_H__

#include <vector>
#include <string>
#include <ctime>
#include <thread>
#include <mutex>

#include "curl_parse.h"

static std::mutex my_mtx;

void thread_func(std::vector<std::string> *urls, std::string dirname, int index);

double calc_multi_threads_work(std::vector<std::string> urls, std::string dirname, int col_threads, int col_exps = 10);

#endif
