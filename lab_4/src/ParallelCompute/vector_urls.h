#ifndef VECTOR_URLS_H__
#define VECTOR_URLS_H__

#include <string>
#include <vector>
#include <fstream>

void read_urls_from_file(std::vector<std::string>& urls, std::string filename, int max_col);

#endif

