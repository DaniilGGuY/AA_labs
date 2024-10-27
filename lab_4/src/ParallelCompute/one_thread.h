#ifndef ONE_THREAD_H__
#define ONE_THREAD_H__

#include <vector>
#include <string>
#include <ctime>

#include "curl_parse.h"

double calc_one_thread_work(std::vector<std::string> urls, std::string dirname, int col_exps = 10);

#endif
