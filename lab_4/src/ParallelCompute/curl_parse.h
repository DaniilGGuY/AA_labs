#ifndef CURLE_PARSE_H__
#define CURLE_PARSE_H__

#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <fstream>

#include "curl/curl.h"

size_t write_data(char* contents, size_t size, size_t nmemb, std::string* response);

void url_to_string(std::string url, std::string filename);

#endif