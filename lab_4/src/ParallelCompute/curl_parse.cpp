#include "curl_parse.h"

size_t write_data(char* contents, size_t size, size_t nmemb, std::string* response)
{
    response->append(contents, size * nmemb);
    return size * nmemb;
}

void url_to_string(std::string url, std::string filename) {
    CURL* curl = curl_easy_init();
    std::string result;

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &result);
        curl_easy_perform(curl);

        curl_easy_cleanup(curl);
    }
    
    std::ofstream out(filename);
    out << result;
    out.close();
}